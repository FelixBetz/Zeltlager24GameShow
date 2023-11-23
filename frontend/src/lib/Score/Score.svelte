<script lang="ts">
	import AvatarImage from '$lib/AvatarImage.svelte';

	import type { Team } from '$lib/types';
	//https://www.learnui.design/tools/data-color-picker.html#single
	const COLORS = ['#f3b84d', '#e49339', '#d36e2c', '#be4825', '#a61a21'];

	const HEIGHT = 60;
	const IMAGE_HEIGHT = 2 * HEIGHT;

	interface BarValue {
		color: string;
		value: number;
	}

	interface ProgressBar {
		values: BarValue[];
	}

	export let teams: Team[] = [];

	let bars: ProgressBar[] = [];
	$: generateProgressBars(teams);
	function generateProgressBars(pTeams: Team[]) {
		let MAX_SCORE = 0;

		pTeams.forEach((team) => {
			let totalScore = team.scores.reduce((acc, currentValue) => acc + currentValue, 0);
			team.total_score = totalScore;
			MAX_SCORE = Math.max(totalScore, MAX_SCORE);
		});

		bars = [];
		pTeams.forEach((team) => {
			let values: BarValue[] = [];
			team.scores.forEach((score, idx) => {
				for (let i = 0; i < score; i++) {
					values.push({ color: COLORS[idx % COLORS.length], value: (1 * 100) / MAX_SCORE });
				}
			});
			bars.push({ values: values });
		});
	}
</script>

<div>
	{#each bars as bar, barIdx}
		<div class=" mt-5 mb-5" style="display:flex;">
			<div class="" style="flex: 1;">
				<div><h1>Team {teams[barIdx].name}: {teams[barIdx].total_score} Punkte</h1></div>
				<div style="width: 100%; display:flex; ">
					{#each bar.values as value, valueIdx}
						<div
							class=" border-dark border-3 point"
							style="width: {value.value}%; background-color: {value.color}; padding:10px; height: {HEIGHT}px; "
							aria-valuenow={value.value}
							aria-valuemin="0"
							aria-valuemax="100"
						/>
					{/each}
				</div>
			</div>
			<div class="ms-5">
				<AvatarImage avatar={teams[barIdx].avatar_url} size={IMAGE_HEIGHT} />
			</div>
		</div>
	{/each}
</div>

<style>
	.point {
		border-right: 1px solid;
		font-weight: bolder;
		font-size: 1.3rem;
	}

	.point:first-child {
		border-bottom-left-radius: var(--bs-border-radius-xl) !important;
		border-top-left-radius: var(--bs-border-radius-xl) !important;
	}

	.point:last-child {
		border-bottom-right-radius: var(--bs-border-radius-xl) !important;
		border-top-right-radius: var(--bs-border-radius-xl) !important;
	}
</style>
