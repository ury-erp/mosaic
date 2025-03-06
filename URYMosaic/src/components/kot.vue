<template>
    <!-- <div class="container mx-auto p-3 mb-16 relative"> -->
    <div class="w-full pl-3 mb-12 relative">
        <!-- Alert Modal div start-->
        <div
            v-if="this.showModal"
            class="fixed inset-0 z-10 overflow-y-auto bg-gray-500 bg-opacity-50"
            @click="this.showModal = false"
        >
            <div class="mt-20 flex items-center justify-center">
                <div class="w-full rounded-lg bg-white p-6 shadow-lg md:max-w-md">
                    <p
                        class="block text-right text-xl font-medium text-gray dark:text-gray"
                    >
                        <span
                            class="w-3 h-3 rounded-full inline-block mr-1 bg-red-500"
                        ></span>
                        غير مصرح
                    </p>
                    <hr class="border-gray-200" />

                    <p class="text-right text-xl mt-6 font-medium text-gray-500">
                        قم بتسجيل الدخول للوصول للصفحة.
                    </p>

                    <div class="flex justify">
                        <button
                            @click="
                            this.showModal = false;
                            this.redirectToLogin();
                            "
                            class="mt-8 rounded bg-blue-500 px-3 py-2 text-white hover:bg-blue-600"
                        >
                            تسجيل الدخول
                        </button>
                    </div>
                </div>
            </div>
        </div>
        <!-- Alert Modal div end-->

        <!-- loading skeleton -->
        <!-- <div v-if="loading" class="flex flex-row-reverse flex-nowrap overflow-x-auto space-x-4 py-2 px-3 h-[calc(100vh-120px)]">
            <div v-for="n in 4" class="flex flex-col flex-shrink-0 w-80 shadow-lg gap-4 p-3 rounded-2xl h-[calc(100vh-140px)] mx-2 kot-card bg-gray-100 animate-pulse"></div>
        </div> -->

        <!-- <div class="mt-5 grid grid-cols-1 gap-10 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4"> -->
        <div class="flex flex-row-reverse flex-nowrap overflow-x-auto space-x-4 py-2 px-3 h-[calc(100vh-120px)]">
            <div v-for="kot in this.kot" :key="kot.name">
                <!-- <div
                    :class="[kot.color]"
                    class="inline-block shadow-lg gap-4 p-3 rounded-2xl w-90 h-auto masonry-item"
                    style="margin-top: 28px"
                    v-if="!kot.showDiv"
                > -->
                <div
                    :class="[
                        kot.color,
                        'flex flex-col flex-shrink-0 w-80 shadow-lg gap-4 p-3 rounded-2xl h-[calc(100vh-140px)] mx-2 kot-card relative',
                        {
                            'pulsing-border': (kot.timeRemaining >= (kot.preparation_time - 1) && kot.type !== 'Cancelled' && kot.type !== 'Partially cancelled')
                        },
                    ]"
                    v-if="!kot.showDiv"
                >
                    <!-- <div class="w-80 check"> -->
                    <div class="w-full kot-content">
                        <div
                            :class="[{ hidden: !kot.isRotated }]"
                            @click="
                                (((userRole.includes(production_units_roles_map[kot.production]['role_responsible_for_serving_kot'])) && (kot.type !== 'Cancelled' && kot.type !== 'Partially cancelled')) && rotateCard(kot)) ||
                                (((userRole.includes(production_units_roles_map[kot.production]['role_responsible_for_confirming_cancelled_kot'])) && (kot.type === 'Cancelled' || kot.type === 'Partially cancelled')) && rotateCard(kot))
                            "
                            class="absolute inset-0 bg-white z-50 opacity-80 rounded-2xl flex flex-col justify-center items-center"
                        >
                            <button
                                @click="
                                    (kot.type !== 'Cancelled' && kot.type !== 'Partially cancelled' && userRole.includes(production_units_roles_map[kot.production]['role_responsible_for_serving_kot']))
                                    ? serveOrder(kot)
                                    : (kot.type === 'Cancelled' || kot.type === 'Partially cancelled') && userRole.includes(production_units_roles_map[kot.production]['role_responsible_for_confirming_cancelled_kot'])
                                    ? confirmOrder(kot)
                                    : null
                                "
                                :class="[{ hidden: !kot.isRotated }]"
                                class="py-2 px-6 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition duration-300 ease-in-out"
                            >
                                {{
                                    (kot.type !== 'Cancelled' && kot.type !== 'Partially cancelled' && userRole.includes(production_units_roles_map[kot.production]['role_responsible_for_serving_kot']))
                                    ? $t('serve')
                                    : (kot.type === 'Cancelled' || kot.type === 'Partially cancelled') && userRole.includes(production_units_roles_map[kot.production]['role_responsible_for_confirming_cancelled_kot'])
                                    ? $t('confirm')
                                    : ""
                                }}
                            </button>
                        </div>
                        <div>
                            <!-- Serve Button -->

                            <!-- Card Header: Table Name and Order Number -->
                            <div class="border-b border-2px border-gray-800 pb-2">
                                <div
                                    class="flex justify-between hover:cursor-pointer"
                                    @click="
                                        (((userRole.includes(production_units_roles_map[kot.production]['role_responsible_for_serving_kot'])) && (kot.type !== 'Cancelled' && kot.type !== 'Partially cancelled')) && rotateCard(kot)) ||
                                        (((userRole.includes(production_units_roles_map[kot.production]['role_responsible_for_confirming_cancelled_kot'])) && (kot.type === 'Cancelled' || kot.type === 'Partially cancelled')) && rotateCard(kot))
                                    "
                                >
                                    <div class="text-sm w-50">
                                        <span
                                            v-if="!is_role_responsible_for_serving_kot && !is_restaurant_manager"
                                            class="text-sm font-medium text-[#6B7280]"
                                        >{{ $t('kitchenUnit') }}:
                                        </span>
                                        <span
                                            v-if="!is_role_responsible_for_serving_kot && !is_restaurant_manager"
                                            class="text-black-500 mr-2 font-semibold"
                                        >
                                            {{ kot.production }}
                                        </span>
                                        <br v-if="!is_role_responsible_for_serving_kot && !is_restaurant_manager">
                                        <!-- v-if="kot.tableortakeaway !== 'Takeaway'" -->
                                        <span
                                            v-if="!kot.table_takeaway"
                                            class="text-sm font-medium text-[#6B7280]"
                                        >{{ $t('table') }}:
                                        </span>
                                        <span class="text-black-500 font-semibold">
                                            {{ kot.tableortakeaway }}
                                            <span class="text-sm font-medium text-[#6B7280]">
                                                ( {{ kot.user }} )
                                            </span
                                        ></span>
                                        <br />
                                        <span v-if="kot.is_aggregator" class="text-sm font-medium text-[#6B7280]">التطبيقات الوسيطة</span>
                                        <span v-if="kot.is_aggregator" class="text-black-500 mr-2 font-semibold">
                                            {{ kot.customer_name }}
                                        </span>
                                        <br v-if="kot.is_aggregator" />
                                        <span v-if="kot.is_aggregator" class="text-sm font-medium text-[#6B7280]">مُعرف التطبيق الوسيط</span>
                                        <span v-if="kot.is_aggregator" class="text-black-500 mr-2 font-semibold">
                                            {{ kot.aggregator_id }}
                                        </span>
                                        <br v-if="kot.is_aggregator"/>
                                        <span class="text-sm font-medium text-[#6B7280]">{{ $t('order') }}:</span>
                                        <span class="text-black-500 mr-2 font-semibold text-xs">
                                            <!-- {{ this.daily_order_number ? kot.order_no : kot.invoice.slice(-4) }} -->
                                            {{ this.daily_order_number ? kot.order_no : kot.invoice }}
                                        </span>
                                        <!-- <span
                                            class="text-black-500 mr-2 font-semibold"
                                            v-if="
                                                kot.type === 'Partially cancelled' ||
                                                kot.type === 'Cancelled'
                                            "
                                        >
                                            ( {{ kot.type }} )</span
                                        > -->
                                    </div>
                                    <div
                                        :class="[
                                            (kot.timeRemaining >= (kot.preparation_time - 1) &&
                                            kot.type !== 'Cancelled' &&
                                            kot.type !== 'Partially cancelled') ?
                                            'text-[#DC0000]' :
                                            'text-black'
                                        ]"
                                        class="font-inter font-semibold text-2xl leading-10"
                                    >
                                        <!-- :class="kot.timecolor" -->
                                        {{ kot.timeRemaining }}<span class="text-sm">{{ $t('m') }}</span>
                                        <span class="text-sm text-gray-500">/ {{ kot.preparation_time }}{{ $t('m') }}</span>
                                    </div>
                                </div>
                                <div
                                    v-if="kot.type === 'Duplicate'"
                                    class="text-[#DC0000] font-medium"
                                >
                                    ( Duplicate KOT ( CHECK WITH CAPTAIN ) )
                                </div>
                                <div v-show="kot.comments" class="text-[#6B7280] font-medium border-r-2 border-l-2 pr-1 border-[#6B7280] bg-[#6B7280] bg-opacity-10 rounded">
                                    {{ kot.comments }}
                                </div>
                            </div>
                            <div></div>
                            <div class="">
                                <div
                                    :class="[GetKOTItemColor(kotitem.kot_type, kot.restaurant_table, kot.table_takeaway), 'rounded px-2']"
                                    class="font-semibold justify-between items-center relative"
                                    v-for="kotitem in sortedKotItems(kot)"
                                    :key="kotitem.name"
                                >
                                    <div
                                        @click="
                                            userRole.includes(production_units_roles_map[kot.production]['role_responsible_for_updating_kot_items_status'])
                                            ? toggleItemStrikeThrough(kotitem, kot)
                                            : null
                                        "
                                        class="flex font-semibold justify-between items-center hover:cursor-pointer overflow-hidden"
                                    >
                                    <!-- :class="{
                                        'line-through text-green-700': kotitem.striked,
                                    }" -->
                                    <div class="transition-colors duration-300">
                                        <span class="text-black-100 relative">
                                            - {{
                                                $i18n.locale === 'ar' ? kotitem.item_name :
                                                    $i18n.locale === 'en' ? kotitem.item :
                                                        $i18n.locale === 'aren' ? kotitem.item_name + ' - ' + kotitem.item : kotitem.item_name
                                            }}
                                            <span v-if="kotitem.indicate_course" class="text-sm text-gray-500 mr-1">
                                                ( {{kotitem.course}} )
                                            </span>
                                            <div 
                                                v-if="kotitem.striked"
                                                class="absolute inset-y-1/2 left-0 h-0.5 bg-green-700 animate-strike"
                                                style="transform: translateY(-50%)"
                                            ></div>
                                        </span>
                                        <br />
                                        <span
                                            class="mr-2 text-gray-700 text-sm relative"
                                            v-if="
                                                (is_role_responsible_for_serving_kot || is_restaurant_manager) &&
                                                    (kotitem?.kot_type === 'Partially cancelled' ||
                                                    kotitem?.kot_type === 'Cancelled')"
                                        >
                                            [الكمية السابقة = {{ kotitem.quantity }}]
                                            <br />
                                            <span
                                                class="mr-2 text-gray-500"
                                                style="font-size: 0.70rem; line-height: 0.75rem;"
                                            >
                                                ({{ kotitem.kot_production + " | " + $t(kotitem.kot_type) }})
                                            </span>
                                            <div 
                                                v-if="kotitem.striked"
                                                class="absolute inset-y-1/2 left-0 h-0.5 bg-green-700 animate-strike"
                                                style="transform: translateY(-50%)"
                                            ></div>
                                        </span>
                                        <span
                                            class="mr-2 text-gray-700 text-sm relative"
                                            v-else-if="
                                                (!is_role_responsible_for_serving_kot && !is_restaurant_manager) &&
                                                    (kot?.type === 'Partially cancelled' ||
                                                    kot?.type === 'Cancelled')"
                                        >
                                            [الكمية السابقة = {{ kotitem.quantity }}]
                                            <div 
                                                v-if="kotitem.striked"
                                                class="absolute inset-y-1/2 left-0 h-0.5 bg-green-700 animate-strike"
                                                style="transform: translateY(-50%)"
                                            ></div>
                                        </span>
                                        <span
                                            class="mr-2 text-gray-500 flex items-center relative"
                                            v-if="(is_role_responsible_for_serving_kot || is_restaurant_manager) &&
                                                (kotitem?.kot_type !== 'Partially cancelled' &&
                                                kotitem?.kot_type !== 'Cancelled')"
                                            style="font-size: 0.70rem; line-height: 0.75rem;"
                                        >
                                            ({{ kotitem.kot_production + " | " + $t(kotitem.kot_type) }})
                                            <div
                                                v-if="is_role_responsible_for_serving_kot || is_restaurant_manager"
                                                :class="[
                                                    (kotitem?.timeRemaining >= (kotitem?.preparation_time - 1) &&
                                                    kotitem?.kot_type !== 'Cancelled' &&
                                                    kotitem?.kot_type !== 'Partially cancelled') ?
                                                    'text-[#DC0000]' :
                                                    'text-black'
                                                ]"
                                                class="text-sm mr-1"
                                            >
                                                {{ kotitem?.timeRemaining }}<span class="text-xs">{{ $t('m') }}</span>
                                                <span class="text-xs text-gray-500">/ {{ kotitem?.preparation_time }}{{ $t('m') }}</span>
                                            </div>
                                            <div 
                                                v-if="kotitem.striked"
                                                class="absolute inset-y-1/2 left-0 h-0.5 bg-green-700 animate-strike"
                                                style="transform: translateY(-50%)"
                                            ></div>
                                        </span>
                                    </div>
                                    <div class="relative">
                                        <span class="mr-2 text-black-100">{{ kotitem.qty }}</span>
                                        <div 
                                            v-if="kotitem.striked"
                                            class="absolute inset-y-1/2 left-0 h-0.5 bg-green-700 animate-strike"
                                            style="transform: translateY(-50%)"
                                        ></div>
                                    </div>
                                </div>
                                <div>
                                    <p
                                        v-show="kotitem.comment"
                                        class="mr-2 text-[#6B7280] font-medium border-r-2 pr-1 border-[#6B7280] bg-[#6B7280] bg-opacity-10 rounded relative"
                                    >
                                        {{ kotitem.comment }}
                                        <div 
                                            v-if="kotitem.striked"
                                            class="absolute inset-y-1/2 left-0 h-0.5 bg-green-700 animate-strike"
                                            style="transform: translateY(-50%)"
                                        ></div>
                                    </p>
                                    <hr class="my-1 border-gray-600 mt-1" />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        </div>

        <!-- Audio Alert Message -->
        <div
            v-if="showAudioAlertMessage"
            class="absolute top-1 left-1/2 transform -translate-x-1/2 p-2 font-bold text-2xl text-red-500 text-center"
        >
            {{ $t('alertSound') }}
        </div>

        <div
            v-if="statusMessage"
            :class="[
                'fixed',
                'bottom-10',
                'left-10',
                'p-4',
                'rounded',
                'text-white',
                {
                    'bg-green-500': isOnline,
                    'bg-red-500': !isOnline,
                },
            ]"
            @transitionend="handleTransitionEnd"
        >
            {{ statusMessage }}
        </div>
        <div class="fixed bottom-3 right-4 flex gap-2">
            <button 
                @click="scrollHorizontally(300)"
                class="p-2 bg-gray-200 backdrop-blur shadow-xl rounded-full hover:scale-105 transition-all"
            >
                →
            </button>
            <button 
                @click="scrollHorizontally(-300)"
                class="p-2 bg-gray-200 backdrop-blur shadow-xl rounded-full hover:scale-105 transition-all"
            >
                ←
            </button>
        </div>
    </div>
</template>

<script>
    import { FrappeApp } from "frappe-js-sdk";
    // import Masonry from "masonry-layout";
    import io from "socket.io-client";
    import { useRestaurantSystemSettings } from "@/stores/RestaurantSystemSettings.js";

    let host = window.location.hostname;
    let port = window.location.port;
    let protocol = window.location.protocol;
    let url = port ? `${protocol}//${host}:${port}` : `${protocol}//${host}`;
    window.globalSiteName = '';
    let socket; 

    async function fetchAndSetSiteName() {
        try {
            const response = await fetch('/api/method/ury_mosaic.ury_mosaic.api.ury_kot_display.get_site_name', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            const data = await response.json();
            window.globalSiteName = data.message.site_name;
        } catch (error) {
            console.error('Failed to fetch site name:', error);
        }
    }

    async function initializeSocket() {
        await fetchAndSetSiteName();
        if (window.globalSiteName) {
            let site = window.globalSiteName;
            let site_url = `${url}/${site}`;
            socket = io(site_url,{ withCredentials: true });
            console.log("socket == >",socket)
            socket.on('connect_error', (err) => {
                console.error("Socket connection error:", err);
            }); 
            socket.on('connect', () => {
                console.log('Socket connected:', socket.connected);
            });
        } else {
            console.error('Site name is not set. Socket cannot be initialized.');
        }
    }

    initializeSocket(); // Initialize the socket after fetching the site name

    const frappe = new FrappeApp(url);
    export default {
        // inject: ["$auth", "$socket"],
        data() {
            return {
                kot: [],
                // masonry: null,
                call: frappe.call(),
                production: "",
                branch: "",
                custom_branch_in_english: "",
                // kot_channel_barista: "",
                // kot_channel_kitchen: "",
                kot_channel: "",
                kot_channel_fetch: "",
                clickedItems: new Set(),
                struckThroughItems: {},
                loggeduser: "",
                showModal: false,
                kot_alert_time: "",
                showAudioAlertMessage: false,
                audio_alert: 0,
                isOnline: navigator.onLine,
                statusMessage: "",
                daily_order_number:0,
                system_settings: this.settings,
                userRole: [],
                production_units_roles_map: null,
                is_role_responsible_for_serving_kot: false,
                is_restaurant_manager: false,
                loading: false,
            };
        },
        setup() {
            const settings = useRestaurantSystemSettings();

            return {settings}
        },
        methods: {
            scrollHorizontally(offset) {
                const container = this.$el.querySelector('.overflow-x-auto');
                container.scrollBy({ left: offset, behavior: 'smooth' });
            },
            playAlertSound(path) {
                var currentDomain = window.location.origin;
                var audio_path = currentDomain + path;
                const audio = new Audio(audio_path);
                audio.play();
            },
            async auth() {
                return new Promise((resolve, reject) => {
                    const auth = frappe.auth();
                    auth.getLoggedInUser()
                        .then((user) => {
                            this.loggeduser = user;
                            this.fetch_user_roles().then(() => {
                                resolve();
                            });
                        })
                        .catch((error) => {
                            console.error(error);
                            reject(error);
                        });
                });
            },
            async fetch_user_roles() {
                this.call
                    .get("ury.ury_pos.api.get_user_roles", this.loggeduser)
                    .then((result) => {
                        this.userRole = result.message;
                    });
            },
            fetchKOT() {
                return new Promise((resolve, reject) => {
                    try {
                        this.call
                            .get("ury_mosaic.ury_mosaic.api.ury_kot_display.kot_list", {})
                            .then((result) => {
                                // console.log(result.message.KOT)
                                this.branch = result.message.Branch;
                                this.custom_branch_in_english = result.message.custom_branch_in_english;
                                this.kot_alert_time = result.message.kot_alert_time;
                                this.audio_alert = result.message.audio_alert;
                                this.daily_order_number = result.message.daily_order_number;
                                this.production_units_roles_map = result.message.production_units_roles_map;

                                // this.kot_channel = `kot_update_${this.branch}_${this.production}`;
                                // this.kot_channel_barista = `kot_update_${this.custom_branch_in_english}_${'barista'}`;
                                // this.kot_channel_kitchen = `kot_update_${this.custom_branch_in_english}_${'kitchen'}`;
                                this.kot_channel = `kot_update_${this.custom_branch_in_english}`;
                                this.kot_channel_fetch = `kot_update_${this.custom_branch_in_english}_fetch`;

                                this.is_role_responsible_for_serving_kot = result.message.is_role_responsible_for_serving_kot;
                                this.is_restaurant_manager = result.message.is_restaurant_manager;
                                
                                this.kot = result.message.KOT;
                                this.updateQtyColorTable();
                                this.updateTimeRemaining();
                                // this.masonryLoading();
                                resolve();
                            })
                            .catch((error) => {
                                console.error(error);
                                reject(error);
                            });
                    } catch (error) {
                        reject(error);
                    }
                });
            },
            rotateCard(kot) {
                // this.masonryLoading();
                kot.isRotated = !kot.isRotated;
            },
            confirmOrder(kot) {
                const now = new Date();
                this.currentTime = now.toLocaleTimeString();
                this.call
                    .post("ury_mosaic.ury_mosaic.api.ury_kot_display.confirm_cancel_kot", {
                        name: kot.name,
                        user: this.loggeduser,
                    })
                    .then((result) => {
                        // kot.isHidden = !kot.isHidden;
                        kot.showDiv = !kot.showDiv;
                        // this.showDiv = false;

                        this.removeAllItemsFromLocalStorage(kot);
                        // this.masonryLoading();
                    })
                    .catch((error) => console.error(error));
            },
            async serveOrder(kot) {
                const now = new Date();
                this.currentTime = now.toLocaleTimeString();

                let method = "ury_mosaic.ury_mosaic.api.ury_kot_display.serve_kot";
                let args = {
                    name: kot.name,
                    time: this.currentTime,
                };

                if(this.is_role_responsible_for_serving_kot) {
                    method = "ury_mosaic.ury_mosaic.api.ury_kot_display.serve_kot_group";
                    args = {
                        names: kot.kot_names || [],
                        time: this.currentTime,
                    };
                }

                this.call
                    .post(method, args)
                    .then((result) => {
                        // kot.isHidden = !kot.isHidden;
                        kot.showDiv = !kot.showDiv;
                        // this.showDiv = false;

                        this.removeAllItemsFromLocalStorage(kot);
                        // this.masonryLoading();
                    })
                    .catch((error) => console.error(error));
            },
            async strikeOrderItem(item) {
                this.call
                    .post("ury_mosaic.ury_mosaic.api.ury_kot_display.strike_kot_item", {
                        item_name: item.name,
                        striked: item.striked,
                    })
                    .then((result) => {
                        
                    })
                    .catch((error) => console.error(error));
            },
            async orderDelayNotify(kot) {
                const now = new Date();
                this.currentTime = now.toLocaleTimeString();

                this.call
                    .post(
                        "ury_mosaic.ury_mosaic.api.ury_kot_notification.order_delay_notification",
                        { id: kot.name, }
                    )
                    .then((result) => {
                        // console.log("call backed ", result);
                    })
                    .catch((error) => console.error(error));
            },
            toggleItemStrikeThrough(kotitem, kot) {
                kotitem.striked = !kotitem.striked;
                this.strikeOrderItem(kotitem);
                // localStorage.setItem(
                //     `${kot.name}_${kotitem.name}_strike`,
                //     JSON.stringify(kotitem.striked)
                // );
            },
            GetKOTItemColor(type, restaurant_table, table_takeaway) {
                if (this.is_role_responsible_for_serving_kot || this.is_restaurant_manager) {
                    if (type == "Order Modified") {
                        return "bg-[#FFD493] border border-[#FFC700]";
                    } else if (type == "Partially cancelled" || type == "Cancelled") {
                        return "bg-[#FFD2D2] border border-[#FAA7A7]";
                    } else if (restaurant_table === undefined || table_takeaway == 1) {
                        return "bg-blue-100 border border-blue-200";
                    } else {
                        return "bg-white";
                    }
                } else {
                    return ''
                }
            },
            updateColorandTable(kot, restaurant_table, type, table_takeaway) {
                if (restaurant_table === undefined) {
                    kot.tableortakeaway = "Takeaway";
                } else {
                    if (table_takeaway == 1) {
                        // kot.tableortakeaway = "Takeaway";
                        kot.tableortakeaway = restaurant_table;
                    } else {
                        kot.tableortakeaway = restaurant_table;
                    }
                }
                if (type == "Order Modified") {
                    kot.color = "bg-[#FFD493] border border-[#FFC700]";
                } else if (type == "Partially cancelled" || type == "Cancelled") {
                    kot.color = "bg-[#FFD2D2] border border-[#FAA7A7]";
                } else if (restaurant_table === undefined || table_takeaway == 1) {
                    kot.color = "bg-blue-100 border border-blue-200";
                } else {
                    kot.color = "bg-white";
                }
            },
            updateQtyColorTable() {
                this.kot.forEach((kot) => {
                    this.updateColorandTable(
                        kot,
                        kot.restaurant_table,
                        kot.type,
                        kot.table_takeaway
                    );

                    kot.kot_items.forEach((kotitem) => {
                        // const savedState = localStorage.getItem(
                        //     `${kot.name}_${kotitem.name}_strike`
                        // );
                        // if (savedState) {
                        //     kotitem.striked = JSON.parse(savedState);
                        // }

                        if(this.is_role_responsible_for_serving_kot || this.is_restaurant_manager) {
                            this.calculateQty(
                                kotitem,
                                kotitem.quantity,
                                kotitem.kot_type,
                                kotitem.cancelled_qty
                            );
                        }
                        else {
                            this.calculateQty(
                                kotitem,
                                kotitem.quantity,
                                kot.type,
                                kotitem.cancelled_qty
                            );
                        }
                    });
                });
            },
            calculateQty(kotitem, qty, type, cancelled_qty) {
                kotitem.qty = qty;
                if (type == "Partially cancelled" || type == "Cancelled") {
                    kotitem.qty = qty - cancelled_qty;
                }
            },
            removeAllItemsFromLocalStorage(kot) {
                // Get all keys in local storage
                const keys = Object.keys(localStorage);
                // Remove keys that start with `${kot.name}_`
                keys.forEach((key) => {
                    if (key.startsWith(`${kot.name}_`)) {
                    localStorage.removeItem(key);
                    }
                });
            },
            updateTimeRemaining() {
                // console.log("update time", this.kot_channel);
                this.kot.forEach((kot) => {
                    if (this.is_role_responsible_for_serving_kot || this.is_restaurant_manager) {
                        kot.kot_items.forEach((kot_item) => {
                            kot_item.timeRemaining = this.calculateTimeElapsed(kot_item?.kot_time, kot_item?.preparation_time);
                        });
                    }
                    
                    kot.timeRemaining = this.calculateTimeElapsed(kot.time, kot.preparation_time);
                    
                    console.log(kot.time);
                    console.log(kot.timeRemaining);

                    const totalElapsedMinutes = kot.timeRemaining;

                    // const [hours, minutes] = kot.timeRemaining.split(":").map(Number);
                    // const totalElapsedMinutes = hours * 60 + minutes;

                    // if (
                    //     totalElapsedMinutes >= (kot.preparation_time - 1) && // Time has exceeded preparation time
                    //     kot.type !== "Cancelled" &&
                    //     kot.type !== "Partially cancelled"
                    // ) {
                    //     kot.timecolor = "text-[#DC0000]"; // Red color
                    // } else {
                    //     kot.timecolor = "text-black"; // Default color
                    // }

                    if (
                        totalElapsedMinutes >= kot.preparation_time &&  // Alert when timer has exceeded preparation time
                        kot.type !== "Cancelled" &&
                        kot.type !== "Partially cancelled"
                    )
                    {
                        this.orderDelayNotify(kot);
                    }

                    // kot.timeRemaining = this.calculateTimeRemaining(kot.time, kot.preparation_time);
                    // console.log(kot.time);
                    // console.log(kot.timeRemaining);

                    // const [hours, minutes] = kot.timeRemaining.split(":").map(Number);
                    // const totalRemainingMinutes = hours * 60 + minutes;

                    // // const timeRemaining = kot.timeRemaining.split(":");
                    // // const minutes =
                    // //   parseInt(timeRemaining[0]) * 60 + parseInt(timeRemaining[1]);

                    // // if (
                    // //   // minutes === this.kot_alert_time &&
                    // //   minutes === kot.preparation_time &&
                    // //   kot.type !== "Cancelled" &&
                    // //   kot.type !== "Partially cancelled"
                    // // )
                    // if (
                    //     totalRemainingMinutes <= 0 &&  // Alert when timer hits 0
                    //     kot.type !== "Cancelled" &&
                    //     kot.type !== "Partially cancelled"
                    // )
                    // {
                    //     this.orderDelayNotify(kot);
                    // }
                    // // if (minutes >= this.kot_alert_time) {
                    // // else if (minutes >= kot.preparation_time) {
                    // if (totalRemainingMinutes <= 1) {
                    //     kot.timecolor = "text-[#DC0000]";
                    // } else {
                    //     kot.timecolor = "text-black";
                    // }
                });
            },
            calculateTimeElapsed(createdTime, preparationTime) {
                const currentTime = new Date();
                const [createdHours, createdMinutes] = createdTime.split(":").map(Number);

                const createdDate = new Date(
                    currentTime.getFullYear(),
                    currentTime.getMonth(),
                    currentTime.getDate(),
                    createdHours,
                    createdMinutes,
                    0
                );

                const elapsedTime = Math.floor((currentTime - createdDate) / 1000); // Elapsed time in seconds
                const totalMinutesElapsed = Math.floor(elapsedTime / 60); // Convert total elapsed seconds to minutes

                return totalMinutesElapsed; // Return the total elapsed time in minutes

                // const elapsedTime = Math.floor((currentTime - createdDate) / 1000); // Elapsed time in seconds

                // const hoursElapsed = Math.floor(elapsedTime / 3600); // 3600 seconds in an hour
                // const minutesElapsed = Math.floor((elapsedTime % 3600) / 60); // Remaining minutes after removing hours

                // const formattedHours = String(hoursElapsed).padStart(2, '0');
                // const formattedMinutes = String(minutesElapsed).padStart(2, '0');

                // if (hoursElapsed === 0) {
                //     return `${minutesElapsed}`; // Return only minutes if no hours
                // }
                // return `${formattedHours} : ${formattedMinutes}`; // Return HH : MM format
            },
            // calculateTimeRemaining(createdTime, preparationTime) {
            //     const currentTime = new Date();
            //     const [createdHours, createdMinutes] = createdTime.split(":").map(Number);

            //     const createdDate = new Date(
            //         currentTime.getFullYear(),
            //         currentTime.getMonth(),
            //         currentTime.getDate(),
            //         createdHours,
            //         createdMinutes,
            //         0
            //     );

            //     const elapsedTime = Math.floor((currentTime - createdDate) / 1000); // Elapsed time in seconds
            //     const totalPreparationSeconds = preparationTime * 60; // Convert preparation time (minutes) to seconds

            //     const remainingSeconds = Math.max(totalPreparationSeconds - elapsedTime, 0); // Prevent negative values

            //     const hoursRemaining = Math.floor(remainingSeconds / 3600); // 3600 seconds in an hour
            //     const minutesRemaining = Math.floor((remainingSeconds % 3600) / 60); // Remaining minutes after removing hours

            //     const formattedHours = String(hoursRemaining).padStart(2, '0');
            //     const formattedMinutes = String(minutesRemaining).padStart(2, '0');
            //     if (hoursRemaining === 0) {
            //         return `${minutesRemaining}`;
            //     }
            //     return `${formattedHours} : ${formattedMinutes}`;
            // },
            fetchkotwithmasonry() {
                return this.fetchKOT().then(() => {
                    // this.masonryLoading();
                });
            },
            redirectToLogin() {
                var currentDomain = window.location.origin;
                window.location.href = currentDomain + "/login?redirect-to=URYMosaic/" + this.production;
            },
            // masonryLoading() {
            //     this.$nextTick(() => {
            //         this.masonry = new Masonry(this.$el.querySelector(".grid"), {
            //             itemSelector: ".masonry-item",
            //             gutter: 28,

            //             // Other Masonry options can be added here
            //         });
            //         this.masonry.layout();
            //     });
            // },
            hideAudioAlertMessage() {
                this.showAudioAlertMessage = false;
            },
            handleOnline() {
                this.isOnline = true;
                this.setStatusMessage("You are online");
                this.hideStatusMessageAfterDelay();
                this.fetchKOT().then(() => {
                    // this.masonryLoading();
                });
            },
            handleOffline() {
                this.isOnline = false;
                this.setStatusMessage("You are Offline");
            },
            setStatusMessage(message) {
                this.statusMessage = message;
            },
            hideStatusMessageAfterDelay() {
                setTimeout(() => {
                    this.statusMessage = "";
                }, 3000);
            },
            handleTransitionEnd() {
                if (!this.isOnline) {
                    // Reset the status message after transition end
                    this.setStatusMessage("");
                }
            },
        },
        beforeUnmount() {
            if(socket) socket.disconnect();
        },
        mounted() {
            window.addEventListener("online", this.handleOnline);
            window.addEventListener("offline", this.handleOffline);
            document.addEventListener("click", this.hideAudioAlertMessage);
            document.addEventListener('keydown', (e) => {
                if(e.key === 'ArrowRight') this.scrollHorizontally(320)
                if(e.key === 'ArrowLeft') this.scrollHorizontally(-320)
            });
            const currentUrl = window.location.href;
            const parts = currentUrl.split("/");
            const production = parts[parts.length - 1];
            const decodedProduction = decodeURIComponent(production);
            this.production = decodedProduction;
            const self = this;
            // window.addEventListener("resize", this.masonryLoading());
            // this.masonryLoading();

            this.auth()
                .then(() => {
                    self.fetchKOT().then(() => {
                        if (this.audio_alert === 1) {
                            this.showAudioAlertMessage = true;
                        }
                        socket.on(this.kot_channel, (doc) => {
                            if (this.is_role_responsible_for_serving_kot || this.is_restaurant_manager) {
                                if (this.audio_alert === 1) {
                                    this.playAlertSound(doc.audio_file);
                                }
                                setTimeout(()=>{
                                    this.fetchKOT().then(() => {
                                        // this.masonryLoading();
                                    });
                                },1500);
                            } else if (
                                this.userRole.includes(doc.production_units_roles_map[doc.kot.production]['role_responsible_for_updating_kot_items_status']) ||
                                this.userRole.includes(doc.production_units_roles_map[doc.kot.production]['role_responsible_for_confirming_cancelled_kot']) ||
                                this.userRole.includes(doc.production_units_roles_map[doc.kot.production]['role_responsible_for_serving_kot']) ||
                                this.userRole.includes("URY Restaurant Manager")
                            ) {
                                if (this.audio_alert === 1) {
                                    this.playAlertSound(doc.audio_file);
                                }
                                let kottime = localStorage.getItem("kot_time");
                                if (doc.last_kot_time !== null) {
                                    if (doc.last_kot_time !== kottime) {
                                        setTimeout(()=>{
                                            this.fetchKOT().then(() => {
                                                // this.masonryLoading();
                                            });
                                        },1500);
                                    }
                                }
                                this.kot.unshift(doc.kot);
                                // this.masonryLoading();
                                this.updateQtyColorTable();
                                this.updateTimeRemaining();
                                setTimeout(()=>{
                                    if (doc.kot.type === "Cancelled"){
                                        this.fetchKOT().then(() => {
                                            // this.masonryLoading();
                                        });
                                    }
                                },1500);
                                localStorage.setItem("kot_time", doc.kot.time);
                            }
                        });
                        
                        socket.on(this.kot_channel_fetch, (event) => {
                            console.log('event', event);
                            this.fetchKOT();
                        });
                    });
                })
            .catch((error) => {
                console.error("Authentication error:", error);
                this.showModal = true;
            });
            setInterval(this.updateTimeRemaining, 60000);
        },
        beforeDestroy() {
            window.removeEventListener("online", this.handleOnline);
            window.removeEventListener("offline", this.handleOffline);
            document.removeEventListener("click", this.hideAudioAlertMessage);
        },
        computed: {
            sortedKotItems() {
                return (kot) => {
                    return kot.kot_items.sort((a, b) => a.serve_priority - b.serve_priority);
                };
            },
        },
    };
</script>

<style scoped>
    .bg-gray-100 {
        background-color: rgba(0, 0, 0, 0.2);
    }

    * {
        user-select: none;
    }

    /* Custom scrollbar styling */
    .overflow-x-auto {
        scrollbar-width: thin !important;
        scrollbar-color: #cbd5e1 transparent;
        scrollbar-gutter: stable;
    }

    .overflow-x-auto::-webkit-scrollbar {
        @apply h-2;
    }

    .overflow-x-auto::-webkit-scrollbar-track {
        @apply bg-gray-200;
    }

    .overflow-x-auto::-webkit-scrollbar-thumb {
        @apply bg-gray-400 rounded-full;
    }

    .overflow-x-auto::-webkit-scrollbar-thumb:hover {
        background: #94a3b8;
    }

    /* KOT item internal scrolling */
    .kot-content {
        overflow-y: auto;
        max-height: calc(100vh - 140px);
        scrollbar-width: thin;
        scrollbar-color: #cbd5e1 transparent;
        scrollbar-gutter: stable;
        padding-left: 8px;
    }

    .kot-card {
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        transition: all 0.2s ease;
    }

    .kot-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 12px -2px rgb(0 0 0 / 0.1);
    }

    /* Remove default margin/padding */
    .container {
        max-width: none !important;
        padding-right: 0;
    }

     @keyframes strike {
        0% { width: 0; }
        100% { width: 100%; }
    }

    .animate-strike {
        animation: strike 0.3s ease-out 0.1s forwards;
    }

    @keyframes fade-in {
        0% { 
            opacity: 0;
            transform: translateY(-10px);
        }
        100% { 
            opacity: 1;
            transform: translateY(0);
        }
    }

    .animate-fade-in {
        animation: fade-in 0.3s ease-out 0.2s;
    }

    @keyframes pulse {
        0% {
            box-shadow: 0 0 0 0 rgba(220, 0, 0, 0.3),
                        0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }
        70% {
            box-shadow: 0 0 0 8px rgba(220, 0, 0, 0),
                        0 8px 12px -2px rgba(0, 0, 0, 0.1);
        }
        100% {
            box-shadow: 0 0 0 0 rgba(220, 0, 0, 0),
                        0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }
    }

    .pulsing-border {
        animation: pulse 1.5s infinite;
        border: 1px solid #DC0000;
        position: relative;
        z-index: 1;
    }
</style>
