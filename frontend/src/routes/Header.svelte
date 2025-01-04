<script>
	import { page } from '$app/stores';
	import github from '$lib/images/github.svg';
</script>

<header
	class="flex sticky z-40 top-0 justify-between items-center p-4 bg-gray-50 border-b border-gray-300"
>
	<div>
		<div class="resume-text">
			<a href="/">
				<span>Resume</span><span class="radar-text">Radar</span>
			</a>
		</div>
	</div>

	<nav>
		<ul class="max-w-screen-xl flex space-x-6">
			<li>
				<a href="/" class="text-gray-800 hover:text-[#F12234]"> Home </a>
			</li>
			<li>
				<a href="/about" class="text-gray-800 hover:text-[#F12234]"> About </a>
			</li>
			<li>
				<a href="https://github.com/blumenlied/ResumeRadar" target="_blank" rel="noopener noreferrer"
					><img src={github} alt="Github" class="w-5 h-5" />
				</a>
			</li>
		</ul>
	</nav>
</header>

<style>
	.resume-text span {
		font-size: 18px;
		font-weight: bold;
		color: black; /* Default color for "Resume" */
		transition: color 0.3s ease;
	}

	.radar-text {
		font-size: 18px;
		font-weight: bold;
		color: black; /* Default color for "Radar" */
		transition: color 0.3s ease;
	}

	.resume-text:hover .radar-text {
		color: #e64553; /* Color for "Radar" when hovered */
	}
</style>
