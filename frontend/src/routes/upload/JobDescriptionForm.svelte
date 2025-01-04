<script>
	export let jobDescription = '';
	export let rows = 6;
	export let isError = false;
	export let errorMessage = 'This field is required.';

	const pasteFromClipboard = async () => {
		try {
			jobDescription = await navigator.clipboard.readText();
		} catch (error) {
			console.error("Failed to read clipboard content:", error);
			alert("Clipboard access is not supported or permission was denied.");
		}
	};
</script>

<div class="mb-4 relative">
	<textarea
		id="jobDescription"
		bind:value={jobDescription}
		{rows}
		class="mt-2 p-2 w-full border text-gray-600 border-gray-300 bg-gray-100 rounded-md"
		placeholder="Paste the job description here..."
	></textarea>
	<button
		type="button"
		on:click={pasteFromClipboard}
		class="absolute top-5 right-4 px-2 py-1 text-sm bg-gray-500 text-white rounded hover:bg-orange-600 transition"
	>
		Paste
	</button>
	{#if isError}
		<div class="text-red-500 text-sm mt-1">{errorMessage}</div>
	{/if}
</div>

