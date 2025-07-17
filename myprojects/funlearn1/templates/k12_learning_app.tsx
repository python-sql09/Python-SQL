import React, { useState, useEffect } from 'react';
import { Play, Pause, RotateCcw, Trophy, Star, Clock, BookOpen, Calculator, Brain, ChevronRight } from 'lucide-react';

const K12LearningApp = () => {
  const [currentGrade, setCurrentGrade] = useState(1);
  const [currentSubject, setCurrentSubject] = useState('math');
  const [currentLevel, setCurrentLevel] = useState(1);
  const [gameState, setGameState] = useState('menu'); // menu, playing, paused, completed
  const [timeLeft, setTimeLeft] = useState(60);
  const [score, setScore] = useState(0);
  const [currentQuestion, setCurrentQuestion] = useState(null);
  const [userAnswer, setUserAnswer] = useState('');
  const [streak, setStreak] = useState(0);
  const [showResult, setShowResult] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);

  const subjects = {
    math: { name: 'Math', icon: Calculator, color: 'bg-blue-500' },
    english: { name: 'English', icon: BookOpen, color: 'bg-green-500' },
    thinking: { name: 'Thinking Skills', icon: Brain, color: 'bg-purple-500' }
  };

  const grades = Array.from({ length: 12 }, (_, i) => i + 1);

  // Question generators for different subjects and grades
  const generateMathQuestion = (grade, level) => {
    const difficulty = Math.min(grade + level - 1, 10);
    
    if (grade <= 2) {
      const a = Math.floor(Math.random() * (5 + difficulty)) + 1;
      const b = Math.floor(Math.random() * (5 + difficulty)) + 1;
      const operations = ['+', '-'];
      const op = operations[Math.floor(Math.random() * operations.length)];
      
      if (op === '-' && a < b) [a, b] = [b, a];
      
      return {
        question: `${a} ${op} ${b} = ?`,
        answer: op === '+' ? a + b : a - b,
        type: 'number'
      };
    } else if (grade <= 5) {
      const a = Math.floor(Math.random() * (10 + difficulty)) + 1;
      const b = Math.floor(Math.random() * (10 + difficulty)) + 1;
      const operations = ['+', '-', '×', '÷'];
      const op = operations[Math.floor(Math.random() * operations.length)];
      
      if (op === '÷') {
        const result = a * b;
        return {
          question: `${result} ÷ ${b} = ?`,
          answer: a,
          type: 'number'
        };
      }
      
      return {
        question: `${a} ${op} ${b} = ?`,
        answer: op === '+' ? a + b : op === '-' ? a - b : a * b,
        type: 'number'
      };
    } else {
      const a = Math.floor(Math.random() * (20 + difficulty)) + 1;
      const b = Math.floor(Math.random() * (20 + difficulty)) + 1;
      const c = Math.floor(Math.random() * 10) + 1;
      
      return {
        question: `Solve: ${a}x + ${b} = ${a * c + b}`,
        answer: c,
        type: 'number'
      };
    }
  };

  const generateEnglishQuestion = (grade, level) => {
    const difficulty = Math.min(grade + level - 1, 10);
    
    if (grade <= 3) {
      const words = ['cat', 'dog', 'run', 'jump', 'happy', 'sad', 'big', 'small', 'red', 'blue'];
      const word = words[Math.floor(Math.random() * words.length)];
      const options = [word, word.split('').reverse().join(''), word.slice(1), word + 'x'];
      
      return {
        question: `Which word is spelled correctly?`,
        options: options.sort(() => Math.random() - 0.5),
        answer: word,
        type: 'multiple'
      };
    } else if (grade <= 6) {
      const sentences = [
        { text: 'The cat is sleeping.', correct: 'The cat is sleeping.' },
        { text: 'she went to school', correct: 'She went to school.' },
        { text: 'i love pizza', correct: 'I love pizza.' }
      ];
      const sentence = sentences[Math.floor(Math.random() * sentences.length)];
      
      return {
        question: `Fix the capitalization: "${sentence.text}"`,
        answer: sentence.correct,
        type: 'text'
      };
    } else {
      const words = ['necessary', 'accommodate', 'definitely', 'separate', 'occurrence'];
      const word = words[Math.floor(Math.random() * words.length)];
      const wrong = word.replace(/e/g, 'a').replace(/a/g, 'e');
      const options = [word, wrong, word.slice(0, -1), word + 'ly'];
      
      return {
        question: `Choose the correct spelling:`,
        options: options.sort(() => Math.random() - 0.5),
        answer: word,
        type: 'multiple'
      };
    }
  };

  const generateThinkingQuestion = (grade, level) => {
    const difficulty = Math.min(grade + level - 1, 10);
    
    if (grade <= 3) {
      const patterns = [
        { sequence: [1, 2, 3, 4], next: 5 },
        { sequence: [2, 4, 6, 8], next: 10 },
        { sequence: [1, 3, 5, 7], next: 9 }
      ];
      const pattern = patterns[Math.floor(Math.random() * patterns.length)];
      
      return {
        question: `What comes next: ${pattern.sequence.join(', ')}, ?`,
        answer: pattern.next,
        type: 'number'
      };
    } else if (grade <= 6) {
      const analogies = [
        { question: 'Hot is to Cold as Up is to ___', answer: 'Down', options: ['Down', 'Left', 'Right', 'Forward'] },
        { question: 'Bird is to Sky as Fish is to ___', answer: 'Water', options: ['Water', 'Land', 'Air', 'Tree'] }
      ];
      const analogy = analogies[Math.floor(Math.random() * analogies.length)];
      
      return {
        question: analogy.question,
        options: analogy.options,
        answer: analogy.answer,
        type: 'multiple'
      };
    } else {
      const logic = [
        { question: 'If all roses are flowers, and some flowers are red, then...', answer: 'Some roses might be red', options: ['All roses are red', 'Some roses might be red', 'No roses are red', 'All flowers are roses'] }
      ];
      const problem = logic[Math.floor(Math.random() * logic.length)];
      
      return {
        question: problem.question,
        options: problem.options,
        answer: problem.answer,
        type: 'multiple'
      };
    }
  };

  const generateQuestion = () => {
    let question;
    switch (currentSubject) {
      case 'math':
        question = generateMathQuestion(currentGrade, currentLevel);
        break;
      case 'english':
        question = generateEnglishQuestion(currentGrade, currentLevel);
        break;
      case 'thinking':
        question = generateThinkingQuestion(currentGrade, currentLevel);
        break;
      default:
        question = generateMathQuestion(currentGrade, currentLevel);
    }
    setCurrentQuestion(question);
    setUserAnswer('');
    setShowResult(false);
  };

  const startGame = () => {
    setGameState('playing');
    setScore(0);
    setStreak(0);
    setTimeLeft(60);
    generateQuestion();
  };

  const pauseGame = () => {
    setGameState('paused');
  };

  const resumeGame = () => {
    setGameState('playing');
  };

  const resetGame = () => {
    setGameState('menu');
    setScore(0);
    setStreak(0);
    setTimeLeft(60);
    setCurrentQuestion(null);
    setUserAnswer('');
    setShowResult(false);
  };

  const checkAnswer = () => {
    if (!currentQuestion) return;
    
    const correct = currentQuestion.answer.toString().toLowerCase() === userAnswer.toLowerCase();
    setIsCorrect(correct);
    setShowResult(true);
    
    if (correct) {
      const points = (currentGrade + currentLevel) * 10;
      setScore(score + points);
      setStreak(streak + 1);
    } else {
      setStreak(0);
    }
    
    setTimeout(() => {
      if (correct && currentLevel < 30) {
        setCurrentLevel(currentLevel + 1);
      }
      generateQuestion();
    }, 1500);
  };

  const handleOptionSelect = (option) => {
    setUserAnswer(option);
    setTimeout(checkAnswer, 500);
  };

  // Timer effect
  useEffect(() => {
    if (gameState === 'playing' && timeLeft > 0) {
      const timer = setTimeout(() => setTimeLeft(timeLeft - 1), 1000);
      return () => clearTimeout(timer);
    } else if (timeLeft === 0) {
      setGameState('completed');
    }
  }, [gameState, timeLeft]);

  const SubjectIcon = subjects[currentSubject].icon;

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-100 via-purple-50 to-pink-100">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-800 mb-2">🌟 Learning Adventure</h1>
          <p className="text-gray-600">Interactive learning for K-12 students</p>
        </div>

        {gameState === 'menu' && (
          <div className="max-w-4xl mx-auto">
            {/* Grade Selection */}
            <div className="bg-white rounded-2xl shadow-xl p-6 mb-6">
              <h2 className="text-2xl font-bold text-gray-800 mb-4">Select Grade</h2>
              <div className="grid grid-cols-6 gap-3">
                {grades.map(grade => (
                  <button
                    key={grade}
                    onClick={() => setCurrentGrade(grade)}
                    className={`p-4 rounded-lg font-semibold transition-all ${
                      currentGrade === grade
                        ? 'bg-blue-500 text-white shadow-lg transform scale-105'
                        : 'bg-gray-100 hover:bg-gray-200 text-gray-700'
                    }`}
                  >
                    {grade}
                  </button>
                ))}
              </div>
            </div>

            {/* Subject Selection */}
            <div className="bg-white rounded-2xl shadow-xl p-6 mb-6">
              <h2 className="text-2xl font-bold text-gray-800 mb-4">Choose Subject</h2>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                {Object.entries(subjects).map(([key, subject]) => {
                  const Icon = subject.icon;
                  return (
                    <button
                      key={key}
                      onClick={() => setCurrentSubject(key)}
                      className={`p-6 rounded-xl font-semibold transition-all ${
                        currentSubject === key
                          ? `${subject.color} text-white shadow-lg transform scale-105`
                          : 'bg-gray-100 hover:bg-gray-200 text-gray-700'
                      }`}
                    >
                      <Icon className="w-8 h-8 mx-auto mb-2" />
                      {subject.name}
                    </button>
                  );
                })}
              </div>
            </div>

            {/* Level Selection */}
            <div className="bg-white rounded-2xl shadow-xl p-6 mb-6">
              <h2 className="text-2xl font-bold text-gray-800 mb-4">Current Level: {currentLevel}</h2>
              <div className="flex items-center justify-between">
                <div className="flex items-center space-x-4">
                  <span className="text-sm text-gray-600">Level 1</span>
                  <div className="w-64 bg-gray-200 rounded-full h-2">
                    <div 
                      className="bg-gradient-to-r from-green-400 to-blue-500 h-2 rounded-full transition-all duration-300"
                      style={{ width: `${(currentLevel / 30) * 100}%` }}
                    ></div>
                  </div>
                  <span className="text-sm text-gray-600">Level 30</span>
                </div>
                <div className="flex items-center space-x-2">
                  <button
                    onClick={() => setCurrentLevel(Math.max(1, currentLevel - 1))}
                    className="px-3 py-1 bg-gray-200 rounded-lg hover:bg-gray-300 transition-colors"
                  >
                    -
                  </button>
                  <button
                    onClick={() => setCurrentLevel(Math.min(30, currentLevel + 1))}
                    className="px-3 py-1 bg-gray-200 rounded-lg hover:bg-gray-300 transition-colors"
                  >
                    +
                  </button>
                </div>
              </div>
            </div>

            {/* Start Button */}
            <div className="text-center">
              <button
                onClick={startGame}
                className="bg-gradient-to-r from-green-400 to-blue-500 text-white px-8 py-4 rounded-2xl font-bold text-xl hover:from-green-500 hover:to-blue-600 transition-all transform hover:scale-105 shadow-lg"
              >
                <Play className="w-6 h-6 inline mr-2" />
                Start Adventure!
              </button>
            </div>
          </div>
        )}

        {(gameState === 'playing' || gameState === 'paused') && (
          <div className="max-w-2xl mx-auto">
            {/* Game Header */}
            <div className="bg-white rounded-2xl shadow-xl p-6 mb-6">
              <div className="flex items-center justify-between mb-4">
                <div className="flex items-center space-x-4">
                  <div className={`p-2 rounded-lg ${subjects[currentSubject].color}`}>
                    <SubjectIcon className="w-6 h-6 text-white" />
                  </div>
                  <div>
                    <h2 className="text-xl font-bold text-gray-800">Grade {currentGrade} • {subjects[currentSubject].name}</h2>
                    <p className="text-gray-600">Level {currentLevel}</p>
                  </div>
                </div>
                <div className="flex items-center space-x-4">
                  <div className="flex items-center space-x-2">
                    <Clock className="w-5 h-5 text-gray-500" />
                    <span className="font-semibold text-gray-700">{timeLeft}s</span>
                  </div>
                  <div className="flex items-center space-x-2">
                    <Trophy className="w-5 h-5 text-yellow-500" />
                    <span className="font-semibold text-gray-700">{score}</span>
                  </div>
                  <div className="flex items-center space-x-2">
                    <Star className="w-5 h-5 text-orange-500" />
                    <span className="font-semibold text-gray-700">{streak}</span>
                  </div>
                </div>
              </div>
              
              <div className="flex space-x-2">
                {gameState === 'playing' ? (
                  <button
                    onClick={pauseGame}
                    className="flex items-center space-x-2 bg-yellow-500 text-white px-4 py-2 rounded-lg hover:bg-yellow-600 transition-colors"
                  >
                    <Pause className="w-4 h-4" />
                    <span>Pause</span>
                  </button>
                ) : (
                  <button
                    onClick={resumeGame}
                    className="flex items-center space-x-2 bg-green-500 text-white px-4 py-2 rounded-lg hover:bg-green-600 transition-colors"
                  >
                    <Play className="w-4 h-4" />
                    <span>Resume</span>
                  </button>
                )}
                <button
                  onClick={resetGame}
                  className="flex items-center space-x-2 bg-gray-500 text-white px-4 py-2 rounded-lg hover:bg-gray-600 transition-colors"
                >
                  <RotateCcw className="w-4 h-4" />
                  <span>Reset</span>
                </button>
              </div>
            </div>

            {/* Question Area */}
            {currentQuestion && gameState === 'playing' && (
              <div className="bg-white rounded-2xl shadow-xl p-8">
                <div className="text-center mb-6">
                  <h3 className="text-2xl font-bold text-gray-800 mb-4">{currentQuestion.question}</h3>
                  
                  {currentQuestion.type === 'multiple' && (
                    <div className="grid grid-cols-1 gap-3">
                      {currentQuestion.options.map((option, index) => (
                        <button
                          key={index}
                          onClick={() => handleOptionSelect(option)}
                          className="p-4 bg-gray-100 hover:bg-blue-100 rounded-lg transition-colors text-left font-semibold"
                        >
                          {option}
                        </button>
                      ))}
                    </div>
                  )}
                  
                  {(currentQuestion.type === 'number' || currentQuestion.type === 'text') && (
                    <div className="space-y-4">
                      <input
                        type="text"
                        value={userAnswer}
                        onChange={(e) => setUserAnswer(e.target.value)}
                        className="w-full p-4 border-2 border-gray-300 rounded-lg text-center text-xl font-semibold focus:border-blue-500 focus:outline-none"
                        placeholder="Your answer..."
                        onKeyPress={(e) => e.key === 'Enter' && checkAnswer()}
                      />
                      <button
                        onClick={checkAnswer}
                        className="bg-blue-500 text-white px-6 py-3 rounded-lg font-semibold hover:bg-blue-600 transition-colors"
                      >
                        Submit Answer
                      </button>
                    </div>
                  )}
                </div>
                
                {showResult && (
                  <div className={`text-center p-4 rounded-lg ${
                    isCorrect ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'
                  }`}>
                    <div className="text-2xl mb-2">
                      {isCorrect ? '🎉 Correct!' : '❌ Try Again!'}
                    </div>
                    <div className="font-semibold">
                      {isCorrect ? 'Great job!' : `The answer was: ${currentQuestion.answer}`}
                    </div>
                  </div>
                )}
              </div>
            )}

            {gameState === 'paused' && (
              <div className="bg-white rounded-2xl shadow-xl p-8 text-center">
                <h3 className="text-2xl font-bold text-gray-800 mb-4">Game Paused</h3>
                <p className="text-gray-600 mb-4">Ready to continue your learning adventure?</p>
                <button
                  onClick={resumeGame}
                  className="bg-green-500 text-white px-6 py-3 rounded-lg font-semibold hover:bg-green-600 transition-colors"
                >
                  <Play className="w-5 h-5 inline mr-2" />
                  Resume Game
                </button>
              </div>
            )}
          </div>
        )}

        {gameState === 'completed' && (
          <div className="max-w-2xl mx-auto">
            <div className="bg-white rounded-2xl shadow-xl p-8 text-center">
              <div className="text-6xl mb-4">🏆</div>
              <h3 className="text-3xl font-bold text-gray-800 mb-4">Great Job!</h3>
              <div className="text-xl text-gray-600 mb-6">
                <p>Final Score: <span className="font-bold text-blue-600">{score}</span></p>
                <p>Best Streak: <span className="font-bold text-orange-600">{streak}</span></p>
                <p>Level Reached: <span className="font-bold text-green-600">{currentLevel}</span></p>
              </div>
              <button
                onClick={resetGame}
                className="bg-blue-500 text-white px-8 py-4 rounded-2xl font-bold text-xl hover:bg-blue-600 transition-colors"
              >
                Play Again
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default K12LearningApp;