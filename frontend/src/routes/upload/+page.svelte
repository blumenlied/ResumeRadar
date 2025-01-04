<script>
	import { userScore } from '$lib/stores/data.js';
	import { pdfBase64 } from '$lib/stores/data.js';
	import { goto } from '$app/navigation';
	import { writable } from 'svelte/store';
	import JobDescriptionForm from './JobDescriptionForm.svelte';
	import FileUploadForm from './FileUploadForm.svelte';

	let jobDescription = '';
	let pdfFile = null;
	let responseMessage = '';
	let isSubmitting = false;

	async function handleSubmit() {
		isSubmitting = true;
		responseMessage = '';

		try {
			const formData = new FormData();
			formData.append('resume', pdfFile);
			formData.append('job_description', jobDescription);

			const response = await fetch('http://127.0.0.1:8000/process', {
				method: 'POST',
				body: formData
			});

			if (response.ok) {
				const data = await response.json();
				// Store data
				userScore.set(data.scores);
				pdfBase64.set(data.resume_pdf_file);
				goto('/results');
			} else {
				const error = await response.json();
				responseMessage = `Error: ${error.error}`;
			}
		} catch (error) {
			console.error('Error submitting form:', error);
			responseMessage = 'An error occurred while submitting the form.';
		} finally {
			isSubmitting = false;
		}
	}
</script>

<svelte:head>
    <title>Upload | ResumeRadar</title>
</svelte:head>

<section class="motion-opacity-in-0 motion-translate-y-in-100 motion-blur-in-md flex-col w-full mx-auto max-w-screen-lg mt-9 shadow-md border border-gray-300 rounded-lg p-6 text-center">
	<JobDescriptionForm bind:jobDescription />
	<FileUploadForm bind:pdfFile />

	<button
		type="button"
		disabled={isSubmitting}
		on:click={handleSubmit}
		class="mt-4 px-4 py-2 text-white rounded-full shadow-md bg-gradient-to-r from-[#DF8E1D] via-[#E64553] to-[#DF8E1D] bg-[length:200%_auto] transition-all duration-500 hover:bg-[position:right_center] active:scale-95 {isSubmitting ? 'motion-translate-y-loop-[20%] motion-ease-spring-smooth' : ''}"
	>
		{isSubmitting ? 'Submitting...' : 'Submit'}
	</button>

	{#if responseMessage}
		<pre class="mt-4 text-rose-500 text-sm font-bold">{responseMessage}</pre>
	{/if}
</section>
