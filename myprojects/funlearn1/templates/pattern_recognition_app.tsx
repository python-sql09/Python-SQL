import React, { useState, useEffect } from 'react';

const PatternRecognitionApp = () => {
  const [currentLevel, setCurrentLevel] = useState(1);
  const [score, setScore] = useState(0);
  const [feedback, setFeedback] = useState('');
  const [gameState, setGameState] = useState('playing');
  const [showCelebration, setShowCelebration] = useState(false);
  const [streak, setStreak] = useState(0);
  const [currentTheme, setCurrentTheme] = useState('shapes');
  const [soundEffect, setSoundEffect] = useState('');

  // Theme configurations
  const themes = {
    shapes: {
      name: 'Shapes & Colors',
      icon: '🔵',
      background: 'from-blue-100 via-purple-100 to-pink-100',
      elements: {
        shapes: ['circle', 'square', 'triangle', 'star', 'heart', 'diamond'],
        colors: ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'cyan']
      }
    },
    animals: {
      name: 'Animal Friends',
      icon: '🐶',
      background: 'from-green-100 via-yellow-100 to-orange-100',
      elements: {
        animals: ['🐶', '🐱', '🐰', '🐸', '🐼', '🦊', '🐻', '🐷', '🐵', '🐨', '🦁', '🐯']
      }
    },
    food: {
      name: 'Yummy Food',
      icon: '🍎',
      background: 'from-red-100 via-orange-100 to-yellow-100',
      elements: {
        food: ['🍎', '🍌', '🍓', '🍊', '🍇', '🥕', '🍅', '🥒', '🍋', '🥝', '🍑', '🫐']
      }
    },
    transport: {
      name: 'Transportation',
      icon: '🚗',
      background: 'from-cyan-100 via-blue-100 to-indigo-100',
      elements: {
        transport: ['🚗', '🚕', '🚙', '🚌', '🚎', '🏎️', '🚓', '🚑', '🚒', '🚐', '🛻', '🚚']
      }
    },
    numbers: {
      name: 'Numbers & Math',
      icon: '1️⃣',
      background: 'from-purple-100 via-pink-100 to-rose-100',
      elements: {
        numbers: ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']
      }
    },
    weather: {
      name: 'Weather Fun',
      icon: '☀️',
      background: 'from-sky-100 via-blue-100 to-slate-100',
      elements: {
        weather: ['☀️', '🌙', '⭐', '☁️', '🌧️', '⛈️', '🌈', '❄️', '🌪️', '🌊']
      }
    }
  };

  const [pattern, setPattern] = useState([]);
  const [choices, setChoices] = useState([]);
  const [correctAnswer, setCorrectAnswer] = useState(null);
  const [patternType, setPatternType] = useState('AB'); // AB, ABC, ABAB, ABCD, etc.

  // Sound effect descriptions
  const playSound = (type) => {
    const sounds = {
      correct: '🎵 *Cheerful bell chime*',
      wrong: '🎵 *Gentle whoosh sound*',
      levelUp: '🎵 *Triumphant fanfare*',
      click: '🎵 *Soft pop*',
      newGame: '🎵 *Magical sparkle*'
    };
    setSoundEffect(sounds[type] || '');
    setTimeout(() => setSoundEffect(''), 2000);
  };

  // Pattern type configurations
  const patternTypes = {
    AB: { length: 4, repeat: 2 },
    ABC: { length: 6, repeat: 3 },
    ABAB: { length: 8, repeat: 4 },
    ABCD: { length: 8, repeat: 4 },
    ABCAB: { length: 10, repeat: 5 },
    AABB: { length: 8, repeat: 4 }
  };

  const generatePattern = () => {
    const theme = themes[currentTheme];
    const difficulty = Math.min(Math.floor(currentLevel / 2) + 1, 6);
    
    // Select pattern type based on difficulty
    const availableTypes = Object.keys(patternTypes).slice(0, difficulty);
    const selectedType = availableTypes[Math.floor(Math.random() * availableTypes.length)];
    setPatternType(selectedType);
    
    const config = patternTypes[selectedType];
    let elements = [];
    
    // Get elements based on theme
    if (currentTheme === 'shapes') {
      // Mix of shapes and colors
      if (currentLevel <= 3) {
        elements = theme.elements.colors.slice(0, 3);
      } else {
        elements = theme.elements.shapes.slice(0, Math.min(4, difficulty));
      }
    } else {
      const themeElements = Object.values(theme.elements)[0];
      elements = themeElements.slice(0, Math.min(selectedType.length, difficulty + 1));
    }
    
    let newPattern = [];
    for (let i = 0; i < config.length; i++) {
      const elementIndex = i % elements.length;
      
      if (currentTheme === 'shapes' && currentLevel <= 3) {
        newPattern.push({
          type: 'color',
          value: elements[elementIndex],
          shape: 'circle'
        });
      } else if (currentTheme === 'shapes' && currentLevel > 3) {
        newPattern.push({
          type: 'shape',
          value: elements[elementIndex],
          color: theme.elements.colors[Math.floor(Math.random() * 3)]
        });
      } else {
        newPattern.push({
          type: currentTheme.slice(0, -1), // Remove 's' from theme name
          value: elements[elementIndex]
        });
      }
    }
    
    return newPattern;
  };

  const generateChoices = (pattern) => {
    const patternLength = pattern.length;
    const repeatLength = patternLength / Math.ceil(patternLength / 4);
    const nextInPattern = pattern[patternLength % Math.floor(repeatLength)];
    const correctChoice = { ...nextInPattern };
    
    let wrongChoices = [];
    const theme = themes[currentTheme];
    
    if (correctChoice.type === 'color') {
      const otherColors = theme.elements.colors.filter(c => c !== correctChoice.value);
      wrongChoices = [
        { ...correctChoice, value: otherColors[0] },
        { ...correctChoice, value: otherColors[1] }
      ];
    } else if (correctChoice.type === 'shape') {
      const otherShapes = theme.elements.shapes.filter(s => s !== correctChoice.value);
      wrongChoices = [
        { ...correctChoice, value: otherShapes[0] },
        { ...correctChoice, value: otherShapes[1] }
      ];
    } else {
      const currentElements = Object.values(theme.elements)[0];
      const otherElements = currentElements.filter(e => e !== correctChoice.value);
      wrongChoices = [
        { type: correctChoice.type, value: otherElements[0] },
        { type: correctChoice.type, value: otherElements[1] }
      ];
    }
    
    const allChoices = [correctChoice, ...wrongChoices];
    return allChoices.sort(() => Math.random() - 0.5);
  };

  const startNewRound = () => {
    playSound('newGame');
    const newPattern = generatePattern();
    setPattern(newPattern);
    
    const patternLength = newPattern.length;
    const repeatLength = patternLength / Math.ceil(patternLength / 4);
    const nextItem = newPattern[patternLength % Math.floor(repeatLength)];
    setCorrectAnswer(nextItem);
    
    setChoices(generateChoices(newPattern));
    setGameState('playing');
    setFeedback('');
    setShowCelebration(false);
  };

  useEffect(() => {
    startNewRound();
  }, [currentLevel, currentTheme]);

  const handleChoice = (choice) => {
    if (gameState !== 'playing') return;
    
    playSound('click');
    const isCorrect = choice.value === correctAnswer.value;
    
    if (isCorrect) {
      setScore(score + (10 * currentLevel));
      setStreak(streak + 1);
      playSound('correct');
      
      const encouragements = [
        'Fantastic! 🎉', 'Amazing work! ⭐', 'You\'re brilliant! 🌟', 
        'Perfect! 💫', 'Excellent! 🎊', 'Great job! 👏'
      ];
      setFeedback(encouragements[Math.floor(Math.random() * encouragements.length)]);
      setGameState('correct');
      setShowCelebration(true);
      
      if (streak > 0 && (streak + 1) % 5 === 0) {
        playSound('levelUp');
      }
      
      setTimeout(() => {
        if (currentLevel < 20) {
          setCurrentLevel(currentLevel + 1);
        } else {
          startNewRound();
        }
      }, 2000);
    } else {
      playSound('wrong');
      const encouragements = [
        'Try again! You can do it! 🤔', 'Almost there! Keep going! 💪',
        'Give it another try! 🌈', 'You\'re learning! Try again! 📚'
      ];
      setFeedback(encouragements[Math.floor(Math.random() * encouragements.length)]);
      setGameState('wrong');
      setStreak(0);
      
      setTimeout(() => {
        setGameState('playing');
        setFeedback('');
      }, 1500);
    }
  };

  const renderElement = (item, size = 'w-20 h-20', isChoice = false) => {
    const baseClasses = `${size} mx-2 flex items-center justify-center text-3xl font-bold rounded-xl border-3 shadow-lg transition-all duration-200 ${
      isChoice ? 'hover:scale-110 active:scale-95 cursor-pointer border-gray-300 hover:border-purple-400' : 'border-gray-200'
    }`;
    
    // Handle emoji-based themes
    if (['animal', 'food', 'transport', 'number', 'weather'].includes(item.type)) {
      return (
        <div className={`${baseClasses} bg-gradient-to-br from-white to-gray-100 text-4xl border-4 ${
          isChoice ? 'hover:from-yellow-100 hover:to-orange-100' : ''
        }`}>
          {item.value}
        </div>
      );
    }
    
    // Handle shapes and colors
    const colorClasses = {
      red: 'bg-gradient-to-br from-red-400 to-red-600',
      blue: 'bg-gradient-to-br from-blue-400 to-blue-600',
      green: 'bg-gradient-to-br from-green-400 to-green-600',
      yellow: 'bg-gradient-to-br from-yellow-400 to-yellow-600',
      purple: 'bg-gradient-to-br from-purple-400 to-purple-600',
      orange: 'bg-gradient-to-br from-orange-400 to-orange-600',
      pink: 'bg-gradient-to-br from-pink-400 to-pink-600',
      cyan: 'bg-gradient-to-br from-cyan-400 to-cyan-600'
    };
    
    const shapeStyles = {
      circle: 'rounded-full',
      square: 'rounded-xl',
      triangle: 'rounded-xl',
      star: 'rounded-xl',
      heart: 'rounded-full',
      diamond: 'rounded-xl'
    };
    
    const shapeSymbols = {
      circle: '●',
      square: '■',
      triangle: '▲',
      star: '★',
      heart: '♥',
      diamond: '♦'
    };
    
    return (
      <div className={`${baseClasses} ${colorClasses[item.color || item.value]} ${shapeStyles[item.shape || item.value]} text-white`}>
        {item.type === 'shape' ? shapeSymbols[item.value] : ''}
      </div>
    );
  };

  const resetGame = () => {
    setCurrentLevel(1);
    setScore(0);
    setStreak(0);
    setFeedback('');
    setGameState('playing');
    setShowCelebration(false);
    playSound('newGame');
  };

  const currentThemeConfig = themes[currentTheme];

  return (
    <div className={`max-w-6xl mx-auto p-4 bg-gradient-to-br ${currentThemeConfig.background} min-h-screen`}>
      {/* Sound Effect Display */}
      {soundEffect && (
        <div className="fixed top-4 right-4 bg-white px-4 py-2 rounded-full shadow-lg text-sm font-semibold text-gray-700 z-50">
          {soundEffect}
        </div>
      )}

      {/* Header */}
      <div className="text-center mb-8">
        <h1 className="text-5xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-purple-600 to-pink-600 mb-4">
          {currentThemeConfig.icon} Pattern Detective! 🕵️
        </h1>
        <div className="flex justify-center gap-4 text-lg font-semibold mb-4 flex-wrap">
          <div className="bg-white px-4 py-2 rounded-full shadow-lg border-2 border-purple-200">
            <span className="text-purple-600">Level:</span> <span className="text-purple-800">{currentLevel}</span>
          </div>
          <div className="bg-white px-4 py-2 rounded-full shadow-lg border-2 border-blue-200">
            <span className="text-blue-600">Score:</span> <span className="text-blue-800">{score}</span>
          </div>
          <div className="bg-white px-4 py-2 rounded-full shadow-lg border-2 border-green-200">
            <span className="text-green-600">Streak:</span> <span className="text-green-800">{streak}</span>
          </div>
          <div className="bg-white px-4 py-2 rounded-full shadow-lg border-2 border-orange-200">
            <span className="text-orange-600">Pattern:</span> <span className="text-orange-800">{patternType}</span>
          </div>
        </div>
      </div>

      {/* Theme Selector */}
      <div className="bg-white rounded-2xl shadow-lg p-6 mb-6 border-2 border-gray-200">
        <h3 className="text-2xl font-bold text-center mb-4 text-gray-800">Choose Your Theme! 🎨</h3>
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
          {Object.entries(themes).map(([key, theme]) => (
            <button
              key={key}
              onClick={() => setCurrentTheme(key)}
              className={`p-4 rounded-xl font-semibold transition-all duration-200 transform hover:scale-105 ${
                currentTheme === key 
                  ? 'bg-gradient-to-r from-purple-500 to-pink-500 text-white shadow-lg' 
                  : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
              }`}
            >
              <div className="text-2xl mb-2">{theme.icon}</div>
              <div className="text-sm">{theme.name}</div>
            </button>
          ))}
        </div>
      </div>

      {/* Game Board */}
      <div className="bg-white rounded-3xl shadow-2xl p-8 mb-6 border-4 border-purple-200">
        <h2 className="text-3xl font-bold text-center mb-8 text-gray-800">
          What comes next in this pattern?
        </h2>
        
        {/* Pattern Display */}
        <div className="flex justify-center items-center mb-10 bg-gray-50 rounded-2xl p-6">
          <div className="flex items-center flex-wrap justify-center">
            {pattern.map((item, index) => (
              <React.Fragment key={index}>
                {renderElement(item)}
                {index < pattern.length - 1 && (
                  <div className="mx-3 text-3xl text-gray-400">→</div>
                )}
              </React.Fragment>
            ))}
            <div className="mx-3 text-3xl text-gray-400">→</div>
            <div className="w-20 h-20 mx-2 border-4 border-dashed border-purple-400 rounded-xl flex items-center justify-center text-4xl text-purple-400 bg-purple-50">
              ?
            </div>
          </div>
        </div>

        {/* Answer Choices */}
        <div className="flex justify-center gap-6 mb-8">
          {choices.map((choice, index) => (
            <button
              key={index}
              onClick={() => handleChoice(choice)}
              disabled={gameState !== 'playing'}
              className={`transform transition-all duration-200 ${
                gameState !== 'playing' ? 'cursor-not-allowed opacity-50' : 'cursor-pointer'
              }`}
            >
              {renderElement(choice, 'w-24 h-24', true)}
            </button>
          ))}
        </div>

        {/* Feedback */}
        {feedback && (
          <div className={`text-center text-2xl font-bold mb-4 ${
            gameState === 'correct' ? 'text-green-600' : 'text-orange-600'
          }`}>
            {feedback}
          </div>
        )}

        {/* Celebration Animation */}
        {showCelebration && (
          <div className="text-center text-6xl animate-bounce">
            🎊 🎉 🌟 🎉 🎊
          </div>
        )}
      </div>

      {/* Control Buttons */}
      <div className="flex justify-center gap-4 mb-6">
        <button
          onClick={startNewRound}
          className="bg-gradient-to-r from-blue-500 to-purple-600 text-white px-8 py-4 rounded-full text-xl font-bold hover:from-blue-600 hover:to-purple-700 transform hover:scale-105 transition-all duration-200 shadow-lg"
        >
          New Pattern 🔄
        </button>
        <button
          onClick={resetGame}
          className="bg-gradient-to-r from-orange-500 to-pink-600 text-white px-8 py-4 rounded-full text-xl font-bold hover:from-orange-600 hover:to-pink-700 transform hover:scale-105 transition-all duration-200 shadow-lg"
        >
          Start Over 🏁
        </button>
      </div>

      {/* Instructions */}
      <div className="bg-white rounded-2xl shadow-lg p-6 border-2 border-yellow-200">
        <h3 className="text-2xl font-bold text-center mb-4 text-yellow-800">
          How to Play 🎮
        </h3>
        <div className="text-lg text-gray-700 text-center space-y-2">
          <p>🎨 Pick your favorite theme above</p>
          <p>👀 Look at the pattern carefully</p>
          <p>🤔 Think about what comes next</p>
          <p>👆 Click on the correct answer</p>
          <p>🎯 Keep going to unlock harder patterns!</p>
          <p>🔊 Listen for fun sound effects!</p>
        </div>
      </div>
    </div>
  );
};

export default PatternRecognitionApp;