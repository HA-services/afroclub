/** @odoo-module */

import { useService } from "@web/core/utils/hooks";
import { useState } from "@odoo/owl";

export function useDialer() {
    return useState(useService("ringover_dialer.dialer"));
}