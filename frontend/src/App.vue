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
                receiver: null,
                savingHints: false
            }
        },
        async mounted() {
            this.participantId = window.location.pathname.match(/\/view\/(.+)$/)[1]

            this.loadParticipant()
            this.loadReceiver()
        },
        methods: {
            getLogoUrl: () => logoUrl,
            async loadParticipant() {
                const response = await fetch(`/api/participants/${this.participantId}`)
                const participant = await response.json()

                participant.hints = ["", "", "", "", ""].map((v, i) => {
                    if (participant.hints[i] !== undefined) {
                        return participant.hints[i]
                    }

                    return v
                })

                this.participant = participant
            },
            async loadReceiver() {
                const response = await fetch(`/api/participants/${this.participantId}/receiver`)
                const receiver = await response.json()

                this.receiver = receiver
            },
            async saveHints() {
                this.savingHints = true

                const hints = this.participant.hints.filter(hint => hint.length > 0)
                const response = await fetch(`/api/participants/${this.participantId}/hints`, {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(hints)
                })

                await this.loadParticipant()
                this.savingHints = false
            }
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
            <span>Hello, <strong>{{ participant.name }}</strong>!</span>
        </div>
    </nav>
    <section class="section">
        <div class="notification is-info is-light">
            <span v-if="receiver">You're buying a gift for <strong>{{ receiver.name }}</strong>!</span>
            <loading v-if="!receiver" :transparent="true"></loading>
        </div>
        <div class="box">
            <loading v-if="!receiver" :transparent="true"></loading>
            <div class="content" v-if="receiver">
                <h5 class="title is-5">{{ receiver.name }}'s Hints</h5>
                <ul v-if="receiver.hints.length > 0">
                    <li v-for="hint in receiver.hints">
                        {{ hint }}
                    </li>
                </ul>
                <p v-if="receiver.hints.length == 0">Oops! {{ receiver.name }} hasn't provided a hint.</p>
            </div>
        </div>
        <div class="box">
            <loading v-if="!participant" :transparent="true"></loading>
            <div class="content is-clearfix" v-if="participant">
                <h5 class="title is-5">Your Hints</h5>
                <p>Please enter up to 5 hints which will be shown to the person who's got you.</p>
                <div class="field" v-for="(hint, i) in participant.hints">
                    <input class="input" :disabled="savingHints" type="text" :placeholder="`Hint #${i + 1}`" v-model="participant.hints[i]">
                </div>
                <button class="button is-success is-pulled-right" v-on:click="saveHints" title="Save Hints" :class="{ 'is-loading': savingHints }">Save Hints</button>
            </div>
        </div>
    </section>
</template>