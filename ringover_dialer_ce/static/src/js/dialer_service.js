/** @odoo-module */

import { registry } from "@web/core/registry";
import { DialerModel } from "./dialer_model";
import { browser } from "@web/core/browser/browser";

const dialerService = {
    dependencies: ["notification"],
    start(env, services) {
        const dialerModel = new DialerModel();
        const bus = dialerModel.bus;

        bus.addEventListener("NOTIFICATION", (ev) => {
            setTimeout(() => {
                services.notification.add(
                    ev.detail.text,
                    { type: ev.detail.type }
                )
            }, 200);
        });

        return dialerModel;
    }
};

registry.category("services").add("ringover_dialer.dialer", dialerService);
