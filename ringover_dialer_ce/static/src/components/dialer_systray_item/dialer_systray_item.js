/** @odoo-module */

import { Component, onMounted } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { useDialer } from "../../js/dialer_hook";
import { Dropdown } from "@web/core/dropdown/dropdown";
import { DropdownItem } from "@web/core/dropdown/dropdown_item";

export class DialerSystray extends Component {
    static template = "ringover_dialer.DialerSystray";
    static props = {};
    static components = {};

    setup() {
        super.setup();
        this.dialer = useDialer();
    }

    iconClicked() {
        this.dialer.toggleDialer();
    }
    get dialerStatus() {
        return this.dialer.status;
    }
}

export const systrayItem = {
    Component: DialerSystray,
};

registry.category("systray").add("ringover_dialer.DialerSystray", systrayItem, { sequence: 1000 });
