<script>
	import { onMount } from 'svelte';
	import { pdfBase64 } from '$lib/stores/data.js';
  import * as pdfjs from 'pdfjs-dist';
	$: pdfData = $pdfBase64;

    let loadingTask;
    let canvas;
    let context;
    
    onMount(async () => {
  pdfjsLib.GlobalWorkerOptions.workerSrc = './node_modules/pdfjs-dist/build/pdf.worker.mjs';

		loadingTask = pdfjsLib.getDocument({ data: atob(pdfData) });
		loadingTask.promise.then(
			async (pdf) => {
				console.log('PDF loaded');

				const pageNumber = 1;
				const page = await pdf.getPage(pageNumber);
				console.log('Page loaded');

				const scale = 1.5;
				const viewport = page.getViewport({ scale });

				canvas = document.getElementById('the-canvas');
				context = canvas.getContext('2d');
				canvas.height = viewport.height;
				canvas.width = viewport.width;

				const renderContext = {
					canvasContext: context,
					viewport
				};

				await page.render(renderContext);
				console.log('Page rendered');
			},
			(reason) => {
				console.error('PDF loading error:', reason);
			}
		);
	});
</script>

<svelte:head>
	<title>Results</title>
	<meta name="description" content="Results page" />
</svelte:head>

<canvas class="motion-delay-700 motion-opacity-in-0 motion-translate-x-in-[-50%] motion-blur-in-md fixed shadow-md rounded-md mr-6 max-h-[780px]"id="the-canvas"></canvas>
