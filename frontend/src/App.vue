<script>
    import logoUrl from "./images/logo.png"
    import Loading from "./components/Loading.vue"

    export default {
        components: {
            "loading": Loading
        },
        data() {
            return {
                participantId: null,
                participant: null,
                giver: null
            };
        },
        async mounted() {
            this.participantId = window.location.pathname.match(/\/view\/(.+)$/)[1]

            const participantResponse = await fetch(`/api/participants/${this.participantId}`)
            this.participant = await participantResponse.json()
        },
        methods: {
            getLogoUrl: () => logoUrl
        }
    }
</script>

<template>
    <nav class="navbar has-background-white-bis is-fixed-top">
        <div class="navbar-brand">
            <span class="navbar-item">
                <img :src="getLogoUrl()">
            </span>
        </div>
        <div class="navbar-item navbar-hello" v-if="participant">
            <span>Hello, <strong>{{ participant?.name }}</strong>!</span>
        </div>
    </nav>
</template>