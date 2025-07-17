// Words bank with A-Z coverage
    const wordBank = {
      2: ["AT", "IN", "ON", "UP", "IT", "NO", "MY", "BY", "TO", "WE", "ME", "GO", "IS", "BE", "DO"],
      3: [
        "ANT", "AIR", "ART" "BAT", "BED", "BAD", "CAT", "COW", "CUT" "DOG", "DOT", "DRY", "EYE", "EGG", "EAT", "FUN", "FAN", "FOG" "GET", "GOD", "GUM", "HOT", "HAT", "HER", "ICE", "INK", "ILL"
        "JAM", "JUG" "JET", "KIT", "KEY", "KID", "LAB", "LOG", "LIP", "MAP", "MAT", "MAN" "NET", "NAP", "NUT", "OWL", "ONE", "OUT", "PEN", "POT", "PET", "QUE", "QAT", "QIN" "RAT", "RED", "RUN",
        "SUN", "SIT", "SAD", "TEN", "TEA", "TOP", "URN", "USE", "UPS", "VAN", "VET", "VIA", "WIN", "WEB", "WHY", "SIX", "FOX", "BOX", "YAK", "YEM", "YES", "ZOO", "ZIP", "ZIG" ],
      4: ["ASIA", "again", "About", "BOOK", "CORN", "DOLL", "EAST", "FISH", "HAND", "FOOT", "READ", "JUMP", "KITE", "LION", "TREE", "DUCK", "SHIP", "FORK", "HAIR", "LOOK", "MAZE", "NEAT", "ROOF"],
      5: ["Apple", "ABOVE", "admin", "BOAT", "CART", "DRUM", "EARN", "MANGO", "SNAKE", "GRAPE", "WATER", "SPOON", "SHEET", "CLEAN", "FRUIT", "WRITE"],
      6: ["alarm", "AIRPORT", "Around" "BUS", "COLOR", "DART", "EARTH", "MARKET", "FAMILY", "POCKET", "CANDLE", "BETTER", "BANANA"],
      7: ["ANGEL", "ate", "April", "BOTTLE", "CHICKEN", "DARK","ENGLISH", "GIRAFFE", "KANGAROO", "MONKEY", "PENGUIN", "TIGER", "ZEBRA", "DINOSAUR", "FIRETRUCK"],
      8: ["Angry", "ARROW", "ADORE","BALLOON", "CIRCUS", "DOLPHIN", "ELECTRIC", "FANTASY", "GUITAR", "HOSPITAL", "JOURNEY", "KITCHEN"],
      9: ["animal", "ARRIVE", "Advice", "BICYCLE", "CARNIVAL", "DREAMLAND", "EXPLORER", "FIREWORKS", "GARDENING", "HARMONICA", "INVENTION", "JELLYFISH"],
      10: ["ALPHABET", "anchor", "Artist", "BRAIN", "CROSSWORD", "DANCING", "EXERCISE", "FANTASTIC", "GIGANTIC", "HARMONY", "IMAGINATION", "JUMPING"],
      11: ["Area", "ARTICLE", "arrival", "BREATH", "CELEBRATION", "DISCOVERY", "EXCITING", "GRANDMOTHER", "HAPPINESS", "IMAGINARY", "JOURNEYMAN"],
      12: ["amazing", "Airplane", "ANYTHING", "BRILLIANT", "CREATIVE", "DYNAMIC", "EXTRAORDINARY", "FASCINATING", "GENEROUS", "HILARIOUS", "INSPIRATIONAL", "JOVIAL"],
      13: ["ASTRONAUT", "activity", "Artifact", "BALL", "CHERRY", "DEPARTMENT", "EXHILARATING", "GRACEFUL", "HARMONIOUS", "INNOVATIVE", "JUBILANT"],
      14: ["Adventure", "avocado", "APPRECIATED", "BACK", "COMPUTER", "DISPOSE", "KINDNESS", "LIVELY", "MAGICAL", "NURTURING", "OPTIMISTIC", "PEACEFUL", "QUIETLY", "RESILIENT"],
      15: ["alligator", "ABACUSES", "Adult", "BUTTER","CITY", "DRAMA", "ELEPHANT", "CANDY", "DOLPHIN", "ELEPHANT", "FIREWORKS", "GIRAFFE", "HONEYBEE", "IGLOO", "JELLYBEAN"]
    };

    const allWordsByLevel = [
      [...wordBank[2], ...wordBank[3]].slice(0, 15),
      [...wordBank[2], ...wordBank[3]].slice(0, 21),
      [...wordBank[2], ...wordBank[3]].slice(0, 24),
      [...wordBank[2], ...wordBank[3], ...wordBank[4]].slice(0, 15),
      [...wordBank[3], ...wordBank[4], ...wordBank[5]].slice(0, 21),
      [...wordBank[4], ...wordBank[5], ...wordBank[6]].slice(0, 24),
      [...wordBank[5], ...wordBank[6], ...wordBank[7]].slice(0, 27),
      [...wordBank[6], ...wordBank[7], ...wordBank[8]].slice(0, 15),
      [...wordBank[7], ...wordBank[8], ...wordBank[9]].slice(0, 21),
      [...wordBank[8], ...wordBank[9], ...wordBank[10]].slice(0, 15),
      [...wordBank[9], ...wordBank[10], ...wordBank[11]].slice(0, 21),
      [...wordBank[10], ...wordBank[11], ...wordBank[12]].slice(0, 27),
      [...wordBank[11], ...wordBank[12], ...wordBank[13]].slice(0, 15),
      [...wordBank[12], ...wordBank[13], ...wordBank[14]].slice(0, 21),
      [...wordBank[13], ...wordBank[14], ...wordBank[15]].slice(0, 27)
    ];

    // Learn words A-Z for Learn Mode
    const wordsByLetter = {
      A: "Apple",
      B: "Bat",
      C: "Cat",
      D: "Dog",
      E: "Egg",
      F: "Fish",
      G: "Gum",
      H: "Hat",
      I: "Ink",
      J: "Jam",
      K: "Kit",
      L: "Lip",
      M: "Map",
      N: "Net",
      O: "Owl",
      P: "Pen",
      Q: "Quo",
      R: "Rat",
      S: "Sun",
      T: "Top",
      U: "Urn",
      V: "Van",
      W: "Win",
      X: "Box",
      Y: "Yak",
      Z: "Zoo"
    };

    let currentLevel = 1;
    let words = [];
    let currentWordIndex = 0;
    let currentWord = "";
    let missingIndex = 0;
    let correctLetter = "";
    let score = 0;
    let total = 0;
    let timer;
    let countdown = 15;
    let answered = false;

    // --- PUZZLE MODE FUNCTIONS ---

    function startLevel(level) {
      currentLevel = level;
      words = allWordsByLevel[level - 1].slice();
      shuffle(words);
      currentWordIndex = 0;
      score = 0;
      total = 0;
      document.getElementById("level-title").textContent = `Level ${level}`;
      resetPuzzleUI();
      nextPuzzle();
    }

    function nextPuzzle() {
      if (currentWordIndex >= words.length) {
        document.getElementById("word").textContent = "🎉 Level Complete!";
        document.getElementById("options").innerHTML = "";
        document.getElementById("result").textContent = "";
        document.getElementById("next-btn").style.display = "none";
        document.getElementById("timer").textContent = "";
        document.getElementById("celebrationSound").play();
        return;
      }

      countdown = 15;
      answered = false;

      currentWord = words[currentWordIndex];
      missingIndex = Math.floor(Math.random() * currentWord.length);
      correctLetter = currentWord[missingIndex];

      const displayWord = currentWord
        .split("")
        .map((ch, idx) => (idx === missingIndex ? "_" : ch))
        .join(" ");
      document.getElementById("word").textContent = displayWord;

      createOptions();
      updateScore();
      startTimer();
      document.getElementById("next-btn").style.display = "none";
      document.getElementById("result").textContent = "";
    }

    function createOptions() {
      const options = new Set([correctLetter]);
      while (options.size < 4) {
        options.add(String.fromCharCode(65 + Math.floor(Math.random() * 26)));
      }
      const shuffled = Array.from(options).sort(() => 0.5 - Math.random());
      const container = document.getElementById("options");
      container.innerHTML = "";

      shuffled.forEach((letter) => {
        const btn = document.createElement("button");
        btn.textContent = letter;
        btn.onclick = () => checkAnswer(letter, btn);
        container.appendChild(btn);
      });
    }

    function checkAnswer(selected, btn) {
      if (answered) return;
      answered = true;
      stopTimer();

      total++;
      if (selected === correctLetter) {
        score++;
        document.getElementById("result").textContent = "🎉 Correct!";
        document.getElementById("result").style.color = "#4CAF50";
        document.getElementById("correctSound").play();
      } else {
        document.getElementById("result").textContent = `❌ Wrong! It was '${correctLetter}'`;
        document.getElementById("result").style.color = "#F44336";
        document.getElementById("wrongSound").play();
      }

      const revealedWord = currentWord
        .split("")
        .map((ch, idx) => (idx === missingIndex ? correctLetter : ch))
        .join(" ");
      document.getElementById("word").textContent = revealedWord;

      updateScore();
      currentWordIndex++;
      document.getElementById("next-btn").style.display = "inline-block";
    }

    function updateScore() {
      document.getElementById("score").textContent = `Score: ${score}/${total}`;
    }

    function startTimer() {
      document.getElementById("timer").textContent = `⏱️ Time left: ${countdown}s`;
      timer = setInterval(() => {
        countdown--;
        document.getElementById("timer").textContent = `⏱️ Time left: ${countdown}s`;
        if (countdown <= 0) {
          clearInterval(timer);
          if (!answered) {
            checkAnswer("", null);
          }
        }
      }, 1000);
    }

    function stopTimer() {
      clearInterval(timer);
    }

    function shuffle(arr) {
      for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
      }
    }

    function resetPuzzleUI() {
      document.getElementById("puzzle-container").style.display = "block";
      document.getElementById("score").style.display = "block";
      document.getElementById("timer").style.display = "block";
      document.getElementById("next-btn").style.display = "none";
      document.getElementById("options").style.display = "block";
      document.getElementById("word").style.display = "block";
      document.getElementById("result").textContent = "";
    }

    // --- LEARN MODE FUNCTIONS ---

    function showLearnMode() {
      document.getElementById('learn-container').style.display = 'block';
      document.getElementById('mode-learn').style.display = 'none';
      document.getElementById('mode-puzzle').style.display = 'inline-block';

      // Hide puzzle UI
      document.getElementById('puzzle-container').style.display = 'none';

      const container = document.getElementById('learn-letters');
      container.innerHTML = '';

      for (const letter in wordsByLetter) {
        const btn = document.createElement('button');
        btn.textContent = letter;
        btn.onclick = () => showLearnWord(letter);
        container.appendChild(btn);
      }

      document.getElementById('learn-word').textContent = '';
    }

    function showLearnWord(letter) {
      const word = wordsByLetter[letter];
      const displayDiv = document.getElementById('learn-word');
      displayDiv.textContent = `${letter} is for ${word}`;

      if ('speechSynthesis' in window) {
        const utterance = new SpeechSynthesisUtterance(`${letter}, is for ${word}`);
        speechSynthesis.cancel(); // stop previous
        speechSynthesis.speak(utterance);
      }
    }

    function showPuzzleMode() {
      document.getElementById('learn-container').style.display = 'none';
      document.getElementById('mode-learn').style.display = 'inline-block';
      document.getElementById('mode-puzzle').style.display = 'none';

      document.getElementById('puzzle-container').style.display = 'block';
      startLevel(currentLevel);
    }

    // --- Start first level on load ---
    startLevel(1);