<template>
    <a :href="link" class="inline-flex items-center w-32 ml-auto px-3 py-2 text-sm text-center text-white font-medium rounded-lg bg-lime-600 hover:bg-lime-700 focus:ring-4 focus:outline-none focus:ring-lime-800">
      <slot></slot>
      <svg class="rtl:rotate-180 w-3.5 h-3.5 ms-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 10">
        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 5h12m0 0L9 1m4 4L9 9"/>
      </svg>
    </a>
</template>

<script>
export default {
    name: 'RecipeButton',
    props: {
        link: {
        type: String,
        required: true,
        },
    },
};
</script>
