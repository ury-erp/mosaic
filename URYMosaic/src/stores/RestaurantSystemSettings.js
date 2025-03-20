import { defineStore } from "pinia";
import frappe from "./frappeSdk.js";
import axios from "axios";

axios.defaults.baseURL = frappe.url;

export const useRestaurantSystemSettings = defineStore("restaurant_system_settings", {
    state: () => ({
        restaurant_system_settings: {},
        call: frappe.call(),
        row_count: parseInt(localStorage.getItem('row_count')) || 1,
        fixed_height: localStorage.getItem('fixed_height') || true,
    }),
    getters: {
        get_restaurant_system_settings() {
            return this.restaurant_system_settings;
        },
    },
    actions: {
        async fetch_restaurant_system_settings() {
            await this.call.get("ury.ury_pos.api.getRestaurantSystemSettings").then((result) => {
                this.restaurant_system_settings = result.message;
            })
                .catch((error) => {
                    console.error("Error fetching restaurant system settings:", error);
                });
        },
        toggleRowCount() {
            this.row_count = this.row_count === 1 ? 2 : 1;
            localStorage.setItem('row_count', this.row_count);
        },
        toggleFixedHeight() {
            this.fixed_height = !this.fixed_height;
            localStorage.setItem('fixed_height', this.fixed_height);
        },
    },
});
