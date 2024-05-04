/** @odoo-module */

import { jsonrpc } from "@web/core/network/rpc_service";
import { Reactive } from "@web/core/utils/reactive";
import { EventBus } from "@odoo/owl";

export class DialerModel extends Reactive {
    constructor() {
        super();
        this.bus = new EventBus();
        this.dialerSdk = 'undefined';
        this.status = 'not_ready';            // not_ready|generated|ready

        // When options are ready, generate dialer
        this.getDialerSettings()
            .then((options) => {
                this.generateDialerSDK(options);
            });

        document.addEventListener("click", (ev) => this.manageClickEvent(ev), false);
    }

    /* vvvv Functions vvvv */

    /* Get settings from DB */
    async getDialerSettings() {
        const defaultOptions = {
            type: 'fixed',
            size: 'medium',
            container: null,
            position: {
                top: 'auto',
                bottom: '0px',
                left: 'auto',
                right: '0px',
            },
            animation: false,
            trayicon: false
        };

        let options = defaultOptions;

        return await jsonrpc(
            '/ringover_dialer_ce/settings/get'
        ).then((data) => {
            if (data.size !== undefined) {
                options.size = data.size;
            }
            if (data.trayicon !== undefined) {
                options.trayicon = Boolean(data.trayicon.toLowerCase);
            }
            if (data.position !== undefined) {
                options.position = {
                    top: 'auto',
                    bottom: 'auto',
                    left: 'auto',
                    right: 'auto',
                };
                switch (data.position) {
                    case 'tr':
                        options.position.top = '40px';
                        options.position.right = '0px';
                        break;
                    case 'br':
                        options.position.bottom = '0px';
                        options.position.right = '0px';
                        break;
                    case 'bl':
                        options.position.bottom = '0px';
                        options.position.left = '0px';
                        break;
                    case 'tl':
                        options.position.top = '40px';
                        options.position.left = '0px';
                        break;
                    default:
                        options.position.bottom = '0px';
                        options.position.right = '0px';
                }
            }

            return options;
        })
            .catch((e) => {
                console.error(e);
                return options;
            });
    }

    /* Generate dialer SDK with options */
    generateDialerSDK(options) {
        // Generate dialer
        if ('undefined' === this.dialerSdk) {
            this.dialerSdk = new RingoverSDK(options);
            this.dialerSdk.generate();
        }
        // Dialer generated and operational
        if (this.dialerSdk.checkStatus()) {
            this.status = 'generated';
            this.dialerSdk.hide();
            this.dialerSdk.on('dialerReady', (ev) => { this.status = 'ready'; });
            this.dialerSdk.on('changePage', (ev) => { if (ev.data.page && ev.data.page === 'login') { this.status = 'generated'; } });
            this.dialerSdk.on('ringingCall', (ev) => { if (!this.dialerSdk.isDisplay()) { this.dialerSdk.show(); } });
        }
    }

    /* Toggle the dialer when click on systray icon */
    toggleDialer() {
        // Dialer not ready
        if ('not_ready' === this.status) {
            this.bus.trigger(
                "NOTIFICATION",
                { 'text': 'Dialer not ready', 'type': 'info' }
            );
            return;
        }
        // Dialer not logged in and hidden
        if ('generated' === this.status && !this.dialerSdk.isDisplay()) {
            this.bus.trigger(
                "NOTIFICATION",
                { 'text': 'Please login', 'type': 'info' }
            );
        }
        this.dialerSdk.toggle();
    }

    /* Popup the dialer when click on a phone number */
    popupDialerOnClick(num, action) {
        if ('generated' === this.status) {
            this.bus.trigger(
                "NOTIFICATION",
                { 'text': 'Please login', 'type': 'info' }
            );
        }
        if ('ready' === this.status) {
            this.dialerSdk.dial(num);
        }
        this.dialerSdk.show();
    }

    /* Listener callback on number link, return phone number string */
    manageClickEvent(ev) {
        let num = '';
        let action = 'tel';

        // Click on tel link
        if (
            ev.target.tagName !== undefined
            && ev.target.tagName === 'A'
            && ev.target.outerHTML.includes('href="tel:')
        ) {
            num = ev.target.pathname;
            action = 'tel';
        } else if (
            ev.target.parentElement !== undefined
            && ev.target.parentElement !== null
            && ev.target.parentElement.tagName !== undefined
            && ev.target.parentElement.tagName !== null
            && ev.target.parentElement.tagName === 'A'
            && ev.target.parentElement.outerHTML.includes('href="tel:')
        ) {
            num = ev.target.parentElement.pathname;
            action = 'tel';
        }

        // Prevent default action: select application
        if (num !== '') {
            ev.preventDefault();
            ev.stopImmediatePropagation();
            ev.stopPropagation();

            this.popupDialerOnClick(num, action);
        }
    }
}