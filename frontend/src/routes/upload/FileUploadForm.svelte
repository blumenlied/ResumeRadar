<script>
	export let pdfFile;
	let isDragging = false;
	let errorMessage = '';

	function handleDrop(event) {
		event.preventDefault();
		isDragging = false;

		if (event.dataTransfer && event.dataTransfer.files.length > 0) {
			const file = event.dataTransfer.files[0];

			if (file.type === 'application/pdf') {
				pdfFile = file;
				errorMessage = '';
			} else {
				errorMessage = 'Please upload a valid PDF file.';
			}

			event.dataTransfer.clearData();
		}
	}

	function handleDragOver(event) {
		event.preventDefault();
		isDragging = true;
	}

	function handleDragLeave() {
		isDragging = false;
	}

	// Handle file input change event (when file is selected via file explorer)
	function handleFileInput(event) {
		const file = event.target.files[0];
		if (file && file.type === 'application/pdf') {
			pdfFile = file;
			errorMessage = '';
		} else {
			errorMessage = 'Please upload a valid PDF file.';
		}
	}
</script>

<div>
	<!-- Drag and Drop Zone -->
	<div
		role="region"
		aria-label="File upload area"
		class={`bg-gray-100 border-2 border-dashed rounded-lg p-6 text-center transition-all
      ${isDragging ? 'bg-yellow-100 border-yellow-600' : 'bg-gray-100 border-gray-300'} flex flex-col justify-center min-h-[200px]`}
		on:drop={handleDrop}
		on:dragover={handleDragOver}
		on:dragleave={handleDragLeave}
	>
		{#if pdfFile}
			<p class="text-gray-700 font-semibold">{pdfFile.name} selected</p>
			<br />
		{:else}
			<p class="text-gray-500">
				Drag and drop your <span class="font-semibold text-gray-700">resume</span> here
			</p>
			<p class="text-gray-500">or</p>
		{/if}

		<input
			type="file"
			accept="application/pdf"
			on:change={handleFileInput}
			class="hidden"
			id="fileInput"
		/>

		<!-- Choose file button -->
		<label
			for="fileInput"
			class="hover:scale-110 transition block w-32 mt-2 mx-auto px-4 py-2 border border-gray-300 bg-transparent font-semibold text-gray-500 rounded-full cursor-pointer shadow"
		>
			Choose File
		</label>
		<p class="mt-4 text-sm text-gray-400">Supported formats: PDF</p>
	</div>

	{#if errorMessage}
		<p class="text-red-500 mt-2">{errorMessage}</p>
	{/if}
</div>
