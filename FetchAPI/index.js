function getNewDog() {
	var url = "https://dog.ceo/api/breed/akita/images/random"
    
	console.log("making fetch to", url)
	
	fetch(url)
		.then(resp=>{return resp.json()})
		.then(json=>{
			console.log(json)

			document.getElementById("dogImage").src = json.message
		})

}

function getNewPokemon() {
    value = Math.floor(Math.random() * 890)
	var url = "https://pokeapi.co/api/v2/pokemon/" + value

	console.log("making fetch to", url)
	
	fetch(url)
		.then(resp=>{return resp.json()})
		.then(json=>{
			console.log(json["sprites"])
        

			document.getElementById("pokemon").src = json.sprites.front_default
            val = json.name
            val = val.charAt(0).toUpperCase() + val.slice(1)
            document.getElementById("pokemon").alt = val
		})

}

function getNewPlayer() {
	var url = "https://www.balldontlie.io/api/v1/players"

	console.log("making fetch to", url)
	
	fetch(url)
		.then(resp=>{return resp.json()})
		.then(json=>{
			console.log(json["sprites"])
        

			document.getElementById("pokemon").src = json.sprites.front_default
            val = json.name
            val = val.charAt(0).toUpperCase() + val.slice(1)
            document.getElementById("pokemon").alt = val
		})

    // Call the API to get all players
    fetch('https://www.balldontlie.io/api/v1/players')
        .then(response => response.json())
        .then(data => {
            // Get a random player from the data
            const randomPlayer = data.data[Math.floor(Math.random() * data.data.length)];
            // Set the player name to the HTML element
            document.getElementById('player-name').textContent = randomPlayer.first_name + ' ' + randomPlayer.last_name;
    })
    .catch(error => console.log(error));
}


document.addEventListener("DOMContentLoaded", () => {
  console.log("Hello World!");
});