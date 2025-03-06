<template>
  <!-- <header class="bg-white p-2 flex justify-between items-center"> -->
  <header class="bg-white px-4 py-1.5 flex justify-between items-center h-16">
    <a :href="'#'" class="flex items-center justify-between" v-if="system_settings.restaurant_system_settings.show_erpnext_mosaic_logo">
        <img v-if="system_settings.restaurant_system_settings.show_erpnext_mosaic_logo" :src="ERPNextMosaicLogoPath" alt="" class="h-12 w-auto"/>
    </a>

    <a :href="'#'" class="flex items-center justify-between" v-else>
        <img v-if="system_settings.restaurant_system_settings.show_system_logo_mosaic" :src="MosaicSystemLogoPath" alt="" class="h-10 w-10"/>
        <p v-if="system_settings.restaurant_system_settings.show_system_name_header_mosaic" class="text-blue-700 text-2xl lg:text-3xl md:text-3xl font-bold mx-2"> {{ system_settings.restaurant_system_settings.system_name || "Restaurant Mosaic" }} </p>
    </a>
    <div class="flex items-center">
      <button
          style="user-select: none;"
          class="ml-2 hover:bg-slate-300 text-blue-700 font-semibold px-6 py-1 rounded-md"
          @click="toggleLanguage()"
          :title="
            $i18n.locale == 'ar' ? 'تغيير اللغة إلى English' : '' +
            $i18n.locale == 'en' ? 'العربية & English': '' +
            $i18n.locale == 'aren' ? 'Change Language to العربية': ''
          "
      >
          {{
            $i18n.locale == 'ar' ? 'AR' : '' +
            $i18n.locale == 'en' ? 'EN': '' +
            $i18n.locale == 'aren' ? 'AR & EN': ''
          }}
      </button>
      <button class=" hover:bg-slate-300 text-blue font-semibold px-6 py-1 rounded-md" @click="reloadKOT">
        <svg class="w-6 h-6 text-blue-800 dark:text-blue" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 20">
          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 1v5h-5M2 19v-5h5m10-4a8 8 0 0 1-14.947 3.97M1 10a8 8 0 0 1 14.947-3.97"/> تحديث
        </svg>          
      </button>
    </div>
  </header>
</template>

<script>
  import MosaicSystemLogo from "@/assets/logos/trilogy_icon.png";
  import ERPNextMosaicLogo from "@/assets/logos/erpnext_mosaic_logo.jpg";
  import { useRestaurantSystemSettings } from "@/stores/RestaurantSystemSettings.js";
  // import KOT from './kot.vue';

  export default {
    name: "Header",
    setup() {
      const settings = useRestaurantSystemSettings();

      return {settings}
    },
    data() {
      return {
        MosaicSystemLogoPath: MosaicSystemLogo,
        ERPNextMosaicLogoPath: ERPNextMosaicLogo,
        system_settings: this.settings,
      };
    },
    methods:{
      reloadKOT(){
        // KOT.methods.fetchKOT(this);
        window.location.reload();
      },
      toggleLanguage() {
        const newLang = (
          this.$i18n.locale === 'ar' ? 'en' : (
            this.$i18n.locale === 'en' ? 'aren' : (
              this.$i18n.locale === 'aren' ? 'ar' : 'ar'
            )
          )
        );
        this.$i18n.locale = newLang;
        localStorage.setItem('lang', newLang);
      },
    },
    computed: {
      
    },
  };
</script>
