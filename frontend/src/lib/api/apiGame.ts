import { API_URL } from './apiUrl';
import { GameState, type Game, type Team } from '../types';

export function apiGetGame(): Promise<Game> {
	const response = fetch(API_URL + 'game')
		.then((response) => response.json())
		.then((response: Game) => response)
		.catch((error) => {
			console.log(error);
			return { teams: [], state: GameState.IDLE };
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

export function apiGetCurrentTeam(): Promise<Team> {
	const response = fetch(API_URL + 'get_current_team')
		.then((response) => response.json())
		.catch((error) => {
			console.log(error);
			return undefined;
		});

	return response;
}
