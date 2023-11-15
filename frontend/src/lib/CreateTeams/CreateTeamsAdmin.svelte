<script lang="ts">
	import AvatarImage from '$lib/AvatarImage.svelte';
	import { apiAddTeam, apiUpdateCurrentTeam } from '$lib/api/apiAdmin';
	import { apiGetAvatars } from '$lib/api/apiGame';

	import type { Team } from '$lib/types';
	import { onMount } from 'svelte';

	let avatars: string[] = [];
	let selectedAvatarIdx = -1;
	let team: Team = {
		shortcut: '',
		name: '',
		scores: [],
		total_score: 0,
		avatar_url: '',
		game_life: 0
	};

	function createNewTeam() {
		team.avatar_url = '';
		team.name = '';
		team.shortcut = '';
		team.total_score = 0;
		team.scores = [];
		selectedAvatarIdx = -1;
	}

	function updateUrl(pIdx: number) {
		if (pIdx >= 0 && pIdx < avatars.length) {
			team.avatar_url = avatars[pIdx];
		}
	}
	function onTeamChange(pTeam: Team) {
		console.log(pTeam);

		apiUpdateCurrentTeam(pTeam);
	}

	$: updateUrl(selectedAvatarIdx);
	$: onTeamChange(team);

	onMount(async () => {
		createNewTeam();
		avatars = await apiGetAvatars();
	});
</script>

<div class="row">
	<div class="col-6">
		<form class="row g-3 needs-validation" novalidate>
			<div class="col-md-6">
				<label for="name" class="form-label">Teamname</label>
				<input
					type="text"
					class="form-control"
					id="name"
					placeholder="Teamname"
					bind:value={team.name}
				/>
			</div>
			<div class="col-md-6">
				<label for="shortcut" class="form-label">Kürzel</label>
				<input
					type="text"
					class="form-control"
					id="shortcut"
					placeholder="Kürzel"
					bind:value={team.shortcut}
				/>
			</div>

			<div>
				<div class="avatar-row">
					{#each avatars as avatar, idx}
						<button on:click={() => (selectedAvatarIdx = idx)} class="p-0 m-0">
							<AvatarImage size={50} {avatar} isSelected={idx == selectedAvatarIdx} />
						</button>
					{/each}
				</div>
			</div>

			<div class="col-12">
				<button class="btn btn-primary" type="submit" on:click={() => apiAddTeam(team)}>
					Create Team
				</button>
			</div>
		</form>
	</div>
	<div class="col-6">asfd</div>
</div>

<style>
	.avatar-row {
		display: flex;
		flex-wrap: wrap;
		column-gap: 10px;
		row-gap: 10px;
	}
	.avatar-row button {
		background-color: transparent;
		border: 0px;
	}
</style>
