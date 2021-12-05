<script>
    export default {
        props: {
            transparent: {
                type: Boolean,
                default: false
            }
        }
    }
</script>

<template>
    <div class="loading" :class="{ 'is-transparent': transparent }"></div>
</template>

<style scoped>
    .loading {
        display: flex;
        justify-content: center;
    }

    .loading::after {
        content: "";
        width: 50px;
        height: 50px;
        border: 5px solid #dddddd;
        border-top-color: darkgreen;
        border-radius: 50%;
        transform: rotate(0.16turn);
        animation: loading 0.75s ease infinite;
    }

    .is-transparent::after {
        border: 5px solid rgba(0, 0, 0, 0.15);
        border-top-color: rgba(0, 0, 0, 0.5);
    }

    @keyframes loading {
        /* Safari support */
        from {
            transform: rotate(0turn);
        }

        to {
            transform: rotate(1turn);
        }
    }
</style>