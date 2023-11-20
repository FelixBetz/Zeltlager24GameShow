import { API_URL } from './apiUrl';
import { type Game, getDefaultGame, type CurrentTeam } from '../types';

export function apiGetGame(): Promise<Game> {
	const response = fetch(API_URL + 'game')
		.then((response) => response.json())
		.then((response: Game) => response)
		.catch((error) => {
			console.log(error);
			return getDefaultGame();
		});

	return response;
}

export function apiGetAvatars(): Promise<string[]> {
	const response = fetch(API_URL + 'avatars')
		.then((response) => response.json())
		.catch((error) => {
			console.log(error);
			return [];
		});

	return response;
}

export function apiGetCurrentTeam(): Promise<CurrentTeam> {
	const response = fetch(API_URL + 'get_current_team')
		.then((response) => response.json())
		.catch((error) => {
			console.log(error);
			return undefined;
		});

	return response;
}
