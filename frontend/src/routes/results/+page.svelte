<script>
	import { userScore } from '$lib/stores/data.js';
	import PdfViewer from './PdfViewer.svelte';
	import { Radar } from 'svelte-chartjs';
	import { data } from './data';
	import download from '$lib/images/download.svg';
	import resultFile from '$lib/pdf/ResumeRadarReport.pdf';

	import {
		Chart as ChartJS,
		Title,
		Tooltip,
		Legend,
		PointElement,
		RadialLinearScale,
		LineElement,
		Filler
	} from 'chart.js';

	ChartJS.register(Title, Tooltip, Legend, PointElement, RadialLinearScale, LineElement, Filler);

	$: score = $userScore.scores;
	$: overall = $userScore.overall_score;

	let fullComment = $userScore.overall_comment;
	let typedComment = '';
	let index = 0;

	function typeComment() {
		if (index < fullComment.length) {
			typedComment += fullComment.charAt(index);
			index++;
			setTimeout(typeComment, 5);
		}
	}

	$: {
		if (fullComment) typeComment();
	}

	// Change color based on score value
	function getColor(scoreValue) {
		if (scoreValue < 30) return 'text-red-500';
		else if (scoreValue < 50) return 'text-orange-500';
		else if (scoreValue < 80) return 'text-yellow-500';
		else return 'text-green-500';
	}
</script>

<svelte:head>
	<title>Results | ResumeRadar</title>
</svelte:head>

<!-- Page Content -->
<section>
	<div class="mt-3 mx-auto flex h-screen">
		<!-- PDF Viewer -->
		<div class="w-1/2 h-full bg-gray-100">
			<PdfViewer />
		</div>

		<!-- Intro bar -->
		<div class="ml-2 w-1/2 h-full bg-transparent">
			<div
				class="motion-translate-y-in motion-duration-500 rounded-md shadow-md mb-4 bg-white flex"
			>
				<h1 class="text-xl text-gray-500 m-4">Resume Grading Results</h1>
				<a
					href="/upload"
					class="hover:text-orange-500 transition m-4 ml-auto text-gray-500 rounded-lg"
					>Upload Again</a
				>
				<div class="flex">
					<a
						href={resultFile}
						download="ResumeRadarReport.pdf"
						class="hover:text-orange-500 transition flex m-4 text-gray-500 rounded-lg"
					>
						Download
						<img src={download} alt="Download" class="ml-2 w-5 h-5" />
					</a>
				</div>
			</div>

			<!-- Score Card -->
			<div
				class="motion-translate-y-in motion-duration-1000 mt-0 bg-white rounded-md border shadow-md border-gray-200 flex items-center justify-center"
			>
				<div class="flex-1 mr-8">
					<section class="flex justify-end">
						<h1 class="font-bold text-lg mr-2 text-gray-500">Overall Score</h1>
						<h1 class="text-lg font-bold {getColor(overall)}">{overall}</h1>
					</section>
					<hr class="ml-5 my-2 border border-gray-300" />
					<section class="flex justify-end">
						<h2 class="text-md mr-2 text-gray-500">Relevance</h2>
						<h2 class="text-md font-bold {getColor(score.Relevance.score)}">
							{score.Relevance.score}
						</h2>
					</section>
					<section class="mt-4 flex justify-end">
						<h2 class="text-md mr-2 text-gray-500">Experience</h2>
						<h2 class="text-md font-bold {getColor(score.Experience.score)}">
							{score.Experience.score}
						</h2>
					</section>
					<section class="mt-4 flex justify-end">
						<h2 class="text-md mr-2 text-gray-500">Skill Demonstration</h2>
						<h2 class="text-md font-bold {getColor(score['Skill Demonstration'].score)}">
							{score['Skill Demonstration'].score}
						</h2>
					</section>
					<section class="mt-4 flex justify-end">
						<h2 class="text-md mr-2 text-gray-500">Professionalism</h2>
						<h2 class="text-md font-bold {getColor(score.Professionalism.score)}">
							{score.Professionalism.score}
						</h2>
					</section>
				</div>

				<div class="flex-1 mr-4">
					<Radar
						{data}
						options={{
							scales: {
								r: {
									ticks: { maxTicksLimit: 10, display: false },
									angleLines: { display: false }
								}
							},
							plugins: { legend: { display: false } },
							responsive: true,
							suggestedMin: 0,
							suggestedMax: 50
						}}
					/>
				</div>
			</div>

			<!-- Comment Section -->
			<div
				class="motion-translate-y-in motion-duration-1500 bg-white pt-4 pb-4 mt-4 rounded-md border shadow-md border-gray-200 flex-1"
			>
				<h1 class="px-4 font-bold text-lg ml-4 mt-4 text-[#F32232]">Overall Comment</h1>
				<h2 class="px-4 ml-4 mr-3 my-4 text-gray-500">{typedComment}</h2>
			</div>

			<!-- Feedback Section -->
			<div
				class="motion-translate-y-in motion-duration-2000 bg-white pt-4 pb-4 mt-4 rounded-md border shadow-md border-gray-200 flex-1"
			>
				<h1 class="px-4 font-bold text-lg ml-4 mt-4 text-gray-600">Relevance</h1>
				<div class="border border-gray-300 rounded-md mx-4 my-4">
					<h1 class="px-4 text-lg ml-4 mt-4 {getColor(score.Relevance.score)}">
						{score.Relevance.feedback_title}
					</h1>
					<p class="px-4 ml-4 mr-3 my-4 text-gray-500">{score.Relevance.feedback}</p>
				</div>

				<hr class="mx-5 my-2 border border-gray-200" />

				<h1 class="px-4 font-bold text-lg ml-4 mt-4 text-gray-600">Experience</h1>
				<div class="border border-gray-300 rounded-md mx-4 my-4">
					<h1 class="px-4 text-lg ml-4 mt-4 {getColor(score.Experience.score)}">
						{score.Experience.feedback_title}
					</h1>
					<p class="px-4 ml-4 mr-3 my-4 text-gray-500">{score.Experience.feedback}</p>
				</div>

				<hr class="mx-5 my-2 border border-gray-200" />

				<h1 class="px-4 font-bold text-lg ml-4 mt-4 text-gray-600">Skill Demonstration</h1>
				<div class="border border-gray-300 rounded-md mx-4 my-4">
					<h1 class="px-4 text-lg ml-4 mt-4 {getColor(score['Skill Demonstration'].score)}">
						{score['Skill Demonstration'].feedback_title}
					</h1>
					<p class="px-4 ml-4 mr-3 my-4 text-gray-500">{score['Skill Demonstration'].feedback}</p>
				</div>

				<hr class="mx-5 my-2 border border-gray-200" />

				<h1 class="px-4 font-bold text-lg ml-4 mt-4 text-gray-600">Professionalism</h1>
				<div class="border border-gray-300 rounded-md mx-4 my-4">
					<h1 class="px-4 text-lg ml-4 mt-4 {getColor(score.Professionalism.score)}">
						{score.Professionalism.feedback_title}
					</h1>
					<p class="px-4 ml-4 mr-3 my-4 text-gray-500">{score.Professionalism.feedback}</p>
				</div>
			</div>
		</div>
	</div>
</section>
