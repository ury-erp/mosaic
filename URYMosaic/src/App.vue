<template>
	<Header/>
 	<!-- <div class="bg-slate-300 min-h-screen"><KOT /></div> -->
 	<div class="bg-slate-300"><KOT /></div>
</template>

<script>
import KOT from './components/kot.vue';
import Header from "./components/Header.vue";
import { useRestaurantSystemSettings } from "@/stores/RestaurantSystemSettings.js";

export default {
	
	name: "app",
	components: {
		KOT,
		Header,
	},
	setup() {
        const restaurantSystemSettingsStore = useRestaurantSystemSettings();
        
        return { restaurantSystemSettingsStore };
    },
    async mounted() {
        await this.restaurantSystemSettingsStore.fetch_restaurant_system_settings();
    },
};
</script>

