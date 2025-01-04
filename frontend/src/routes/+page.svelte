<script>
	import sample from '$lib/images/sample.jpg';

	let text =
		'Get instant, actionable feedback on your resume with this AI-powered grading tool designed to help you stand out.';

	let typedText = '';
	let index = 0;
	let isTyping = true;

	function typeText() {
		if (index < text.length) {
			typedText += text.charAt(index);
			index++;
			setTimeout(typeText, 30);
		} else {
			isTyping = false;
		}
	}

	// On load
	$: {
		if (text) typeText();
	}
</script>

<svelte:head>
	<title>ResumeRadar</title>
	<meta name="description" content="Home page" />
</svelte:head>

<section class="flex flex-col justify-center items-center flex-1">
	<h1
		class="mt-[120px] text-6xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-[#DF8E1D] via-[#F32234] to-[#F32234]"
	>
		AI-Powered Resume Grader
	</h1>
	<p class="text-gray-600 p-6">{typedText}</p>

	<a
		href="/upload"
		class="{isTyping
			? 'invisible'
			: 'motion-opacity-in-0 motion-preset-blur-up'} text-white font-bold py-3 px-6 rounded-full shadow-md bg-gradient-to-r from-[#DF8E1D] via-[#E64553] to-[#DF8E1D] bg-[length:200%_auto] transition-all duration-500 hover:bg-[position:right_center] active:scale-95"
	>
		Get started
	</a>

    <img src={sample} alt="Sample" class="{isTyping ? 'invisible' : 'motion-translate-y-in-100 motion-duration-[2s] motion-ease-spring-smooth visible'} mb-[100px] mt-[100px] object-contain border border-gray-300 rounded-md shadow-md" />

    <h1 class="text-gray-500 text-md mb-[40px]">Made by Stephen Cabrejas</h1>
</section>
