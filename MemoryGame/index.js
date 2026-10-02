
// NOTE(Tejas): I think its simple for this game that we use DOM like buttons
// because the game flows like that, but you could use Canvas and take the full
// control of the rendering: I think its simple for this game that we use DOM
// like buttons because the game flows like that, but you could use Canvas and
// take the full control of the rendering.

const TOTAL_PAIRS = 8;
const CARD_VALUES = [ "🍎", "🍌", "🍇", "🍊", "🍓", "🍒", "🍍", "🥝" ];

// NOTE(Tejas): Look at index.html. here we can refer to the stuff in html and
// alter things that are being rendered
const HTMLContext = {
    game_board: document.getElementById("game-board"),
    moves_display: document.getElementById("moves"),
    pairs_display: document.getElementById("pairs"),
    timer_display: document.getElementById("timer"),
    restart_button: document.getElementById("restart-button"),
    game_message: document.getElementById("game-message"),
    completion_summary: document.getElementById("completion-summary"),
    final_moves: document.getElementById("final-moves"),
    final_time: document.getElementById("final-time"),
    final_accuracy: document.getElementById("final-accuracy"),
}

// NOTE(Tejas): Game related stuff
const GameState = {

    lock_board: false,

    first_card: null,
    second_card: null,

    moves: 0,
    matched_pairs: 0,

    start_time: null,
    elapsed_time: 0,
    timer_interval: null,

    game_started: false,
    game_completed: false,
}

// NOTE(Tejas): This is a simple shuffle algorithm that randomly shuffles the
// cards. Look up Fisher-Yates shuffle algorithm.
function shuffle_cards(cards) {

    // NOTE(Tejas): if you are wadering why we did not do `const shuffled = cards;` 
    // it is because that would create a reference to the original array.  
    // Look up Shallow copy vs Deep copy.
    const shuffled = [...cards]; 

    for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }

    return shuffled;
}

function format_time(seconds) {

    const minutes = Math.floor(seconds / 60);
    const remaining_seconds = seconds % 60;

    return (
        String(minutes).padStart(2, "0") +
        ":" +
        String(remaining_seconds).padStart(2, "0")
    );
}

function init_game() {

    HTMLContext.game_board.innerHTML = "";

    // NOTE(Tejas): We have a 2x2 grid of cards, we have every card value twice
    // and then we shuffle the whole 2x2 grid of cards.
    const cards = shuffle_cards([...CARD_VALUES, ...CARD_VALUES]);

    cards.forEach((value, index) => {

        // NOTE(Tejas): these dont exist in the HTML we dynamically create them,
        // our css only knows to put 4 cards across if you see the css of
        // .game-board. We could create any number of here without telling html
        // or css. we just tell them that info to better format the visual
        const card = document.createElement("div");

        // NOTE(Tejas): here we can do stuff that we would normally do in html inside <>.
        card.type = "button";
        card.classList.add("card");

        card.dataset.value = value;
        card.dataset.position = index;

        card.textContent = "?";

        card.setAttribute("aria-label", `Card ${index + 1}, face down`);
        card.addEventListener("click", () => { flip_card(card); });

        HTMLContext.game_board.appendChild(card);
    })
}

function start_timer() {

    if (GameState.timer_interval) return;

    GameState.start_time = Date.now() - GameState.elapsed_time;
    GameState.timer_interval = setInterval(() => {
        GameState.elapsed_time = Date.now() - GameState.start_time;
        HTMLContext.timer_display.textContent = format_time(Math.floor(GameState.elapsed_time / 1000));
    }, 250);
}

function stop_timer() {

    if (GameState.timer_interval !== null) {
        clearInterval(GameState.timer_interval);
        GameState.timer_interval = null;
    }

    if (GameState.start_time !== null) {
        GameState.elapsed_time = Date.now() - GameState.start_time;
        HTMLContext.timer_display.textContent = format_time(Math.floor(GameState.elapsed_time / 1000));
    }
}

function flip_card(card) {
    // NOTE(Tejas): THIS IS NOT THE ANIMATION OF THE CARD FLIPPING.
    // This is the logic of what happends when a player clicks on a card.

    if (GameState.lock_board) return;

    if (GameState.game_completed) return;
    if (card === GameState.first_card) return;

    // NOTE(Tejas): Now instead of maintaining a list of matched and flipped
    // cards, we can just use a clever trick with css. We can just look at the
    // attributes of each card to see if it was flipped or not.
    if (card.classList.contains("matched")) return;
    if (card.classList.contains("flipped")) return;

    if (!GameState.game_started) {
        GameState.game_started = true;
        start_timer();
    }

    card.classList.add("flipped");
    card.textContent = card.dataset.value;

    card.setAttribute("aria-label", `Card ${Number(card.dataset.position) + 1}, ${card.dataset.value}`);

    if (GameState.first_card === null) {
        GameState.first_card = card;
        return;
    }

    GameState.second_card = card;
    GameState.moves++;

    update_stats(); 
    check_for_match();
}

function check_for_match() {

    const is_match = GameState.first_card.dataset.value === GameState.second_card.dataset.value;
    if (is_match) {
        handle_match();
    } else {
        handle_mismatch();
    }
}

function handle_match() {

    GameState.first_card.classList.add("matched");
    GameState.second_card.classList.add("matched");

    // NOTE(Tejas): I just disabled the matched cards here but you can also put
    // them both on display. Up to You.
    GameState.first_card.disabled = true;
    GameState.second_card.disabled = true;

    GameState.matched_pairs++;

    update_stats();

    HTMLContext.game_message.textContent = "Pair Found!";
    reset_turn();

    if (GameState.matched_pairs === TOTAL_PAIRS) {
        complete_game();
    }
}

function handle_mismatch() {

    // NOTE(Tejas): we want to animate the mismatch and show both cards for a
    // second before flipping them back over.

    // NOTE(Tejas): This is the only reason we have lock_board. We want to
    // prevent the user from doing anything while the animation is running.
    GameState.lock_board = true;

    HTMLContext.game_message.textContent = "No Match!";

    setTimeout(() => {

        GameState.first_card.classList.remove("flipped");
        GameState.second_card.classList.remove("flipped");

        GameState.first_card.textContent = "?";
        GameState.second_card.textContent = "?";

        GameState.first_card.setAttribute(
            "aria-label",
            `Card ${Number(GameState.first_card.dataset.position) + 1}, face down`
        );

        GameState.second_card.setAttribute(
            "aria-label",
            `Card ${Number(GameState.second_card.dataset.position) + 1}, face down`
        );

        reset_turn();
        HTMLContext.game_message.textContent = "Find all 8 matching pairs.";

    }, 1000);
}

function reset_turn() {

    GameState.first_card = null;
    GameState.second_card = null;
    GameState.lock_board = false;
}

function update_stats() {

    HTMLContext.moves_display.textContent = GameState.moves;
    HTMLContext.pairs_display.textContent = `${GameState.matched_pairs} / ${TOTAL_PAIRS}`;
}

function calculate_accuracy() {

    if (GameState.moves === 0) return 0;
    return (GameState.matched_pairs / GameState.moves) * 100;
}


function complete_game() {

    GameState.game_completed = true;
    stop_timer();

    const accuracy = calculate_accuracy();

    HTMLContext.final_moves.textContent = GameState.moves;
    HTMLContext.final_time.textContent = HTMLContext.timer_display.textContent;
    HTMLContext.final_accuracy.textContent = `${accuracy.toFixed(2)}%`;
    HTMLContext.completion_summary.hidden = false;

    HTMLContext.game_message.textContent = "Congratulations! You've completed the game!";

    // NOTE(Tejas): Add multiple matrics to this game_stat that you would send
    // to your backend to evalutate the performance.
    const game_stats = {

        game_id: Date.now(),
        total_pairs: TOTAL_PAIRS,
        moves: GameState.moves,
        matched_pairs: GameState.matched_pairs,
        accuracy: accuracy,
        time_taken: HTMLContext.timer_display.textContent,
        completion_time: GameState.elapsed_time,
    }

    // TODO(Tejas): send this to your backend for evaluation and storage.
    console.log("Game Stats:", game_stats); 
}

function restart_game() {

    stop_timer();

    GameState.first_card = null;
    GameState.second_card = null;
    GameState.lock_board = false;

    GameState.moves = 0;
    GameState.matched_pairs = 0;
    GameState.start_time = null;
    GameState.elapsed_time = 0;

    GameState.game_started = false;
    GameState.game_completed = false;

    HTMLContext.completion_summary.hidden = true;
    HTMLContext.game_message.textContent = "Find all 8 matching pairs.";
    HTMLContext.timer_display.textContent = "00:00";
    HTMLContext.moves_display.textContent = "0";
    HTMLContext.pairs_display.textContent = `0 / ${TOTAL_PAIRS}`;

    init_game();
}

HTMLContext.restart_button.addEventListener("click", restart_game);
init_game();
update_stats();