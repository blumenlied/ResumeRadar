<script>
	import '../app.css';
	import Header from './Header.svelte';
</script>

<div class="app flex flex-col min-h-screen">
	<Header />
	<main class="flex-grow flex flex-col p-4 w-full max-w-screen-xl mx-auto box-border">
		<slot />
	</main>
</div>
