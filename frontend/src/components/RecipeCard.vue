<template>
    <div class="flex flex-col place-content-around h-60 p-4 rounded-lg bg-gray-800 border border-gray-700 shadow-md shadow-gray-700">
      <a class="self-center h-2/6" :href="link">
        <h2 class="text-center mb-2 text-xl font-bold tracking-tight text-white">{{ title }}</h2>
      </a>
      <slot></slot>
    </div>
  </template>

  <script>
  export default {
    name: 'RecipeCard',
    props: {
      title: {
        type: String,
        required: true,
      },
      link: {
        type: String,
        required: true,
      },
    },
  };
  </script>
