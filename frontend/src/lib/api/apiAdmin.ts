import type { Team } from '$lib/types';
import { API_URL } from './apiUrl';

export function apiAdminSwitchState(pState: string): Promise<boolean> {
	const response = fetch(API_URL + 'admin/switchState?state=' + pState)
		.then(() => true)
		.catch((error) => {
			console.log(error);
			return false;
		});

	return response;
}

export function apiAddTeam(pTeam: Team): Promise<boolean> {
	const formData = new FormData();
	formData.append('name', pTeam.name);
	formData.append('shortcut', pTeam.shortcut);
	formData.append('avatar_url', pTeam.avatar_url);

	const response = fetch(API_URL + 'add_team', {
		method: 'POST',
		body: formData
	})
		.then(() => true)
		.catch((error) => {
			console.log(error);
			return false;
		});

	return response;
}

export function apiUpdateCurrentTeam(pTeam: Team): Promise<boolean> {
	const formData = new FormData();
	formData.append('name', pTeam.name);
	formData.append('shortcut', pTeam.shortcut);
	formData.append('avatar_url', pTeam.avatar_url);
	const response = fetch(API_URL + 'update_current_team', {
		method: 'POST',
		body: formData
	})
		.then(() => true)
		.catch((error) => {
			console.log(error);
			return false;
		});

	return response;
}

export function apiDeleteTeam(pTeamIdx: number): Promise<boolean> {
	const response = fetch(API_URL + 'deleteTeam?idx=' + pTeamIdx)
		.then(() => true)
		.catch((error) => {
			console.log(error);
			return false;
		});

	return response;
}

export function apiIncrementTeamLife(pTeamIndex: number): Promise<boolean> {
	const response = fetch(API_URL + 'admin/incrementLife?team=' + pTeamIndex.toString())
		.then(() => true)
		.catch((error) => {
			console.log(error);
			return false;
		});

	return response;
}
export function apiDecrementTeamLife(pTeamIndex: number): Promise<boolean> {
	const response = fetch(API_URL + 'admin/decrementLife?team=' + pTeamIndex.toString())
		.then(() => true)
		.catch((error) => {
			console.log(error);
			return false;
		});

	return response;
}
