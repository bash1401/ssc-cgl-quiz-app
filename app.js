/**
 * SSC CGL Exam Practice Suite - 10,000+ Question Engine
 */

(function () {
  'use strict';

  const state = {
    allQuestions: window.SSC_QUESTIONS || [],
    filteredQuestions: [],
    currentIndex: 0,
    subjectFilter: 'all',
    userAnswers: JSON.parse(localStorage.getItem('ssc_user_answers') || '{}'),
    submittedStates: JSON.parse(localStorage.getItem('ssc_submitted_states') || '{}'),
    bookmarks: new Set(JSON.parse(localStorage.getItem('ssc_bookmarks') || '[]')),
    theme: localStorage.getItem('ssc_theme') || 'dark'
  };

  const DOM = {
    themeToggleBtn: document.getElementById('btn-toggle-theme'),
    resetStatsBtn: document.getElementById('btn-reset-stats'),
    openSearchBtn: document.getElementById('btn-open-search'),
    searchModal: document.getElementById('search-modal'),
    closeSearchBtn: document.getElementById('btn-close-search'),
    searchInput: document.getElementById('search-input'),
    searchResultsList: document.getElementById('search-results-list'),
    
    subjectFilterList: document.getElementById('subject-filter-list'),
    questionNavGrid: document.getElementById('question-nav-grid'),
    gridLabel: document.getElementById('grid-label'),
    
    statAnswered: document.getElementById('stat-answered'),
    statAccuracy: document.getElementById('stat-accuracy'),
    statBookmarks: document.getElementById('stat-bookmarks'),
    
    qSubjectBadge: document.getElementById('q-subject-badge'),
    qTopicBadge: document.getElementById('q-topic-badge'),
    qText: document.getElementById('q-text'),
    qOptionsList: document.getElementById('q-options-list'),
    
    btnBookmark: document.getElementById('btn-bookmark'),
    btnPrev: document.getElementById('btn-prev'),
    btnNext: document.getElementById('btn-next'),
    btnSubmit: document.getElementById('btn-submit'),
    btnToggleExplanation: document.getElementById('btn-toggle-explanation'),
    
    explanationBox: document.getElementById('explanation-box'),
    explanationText: document.getElementById('explanation-text')
  };

  function init() {
    setupTheme();
    setupEventListeners();
    applyFilters();
    updateHeaderStats();

    // Keybindings for navigation
    document.addEventListener('keydown', (e) => {
      if (['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) return;
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') nextQ();
      if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') prevQ();
      if (e.key === 'Enter') submitCurrentAnswer();
    });
  }

  function setupTheme() {
    document.documentElement.setAttribute('data-theme', state.theme);
    DOM.themeToggleBtn.textContent = state.theme === 'dark' ? '☀️' : '🌙';
  }

  function toggleTheme() {
    state.theme = state.theme === 'dark' ? 'light' : 'dark';
    localStorage.setItem('ssc_theme', state.theme);
    setupTheme();
  }

  function saveState() {
    localStorage.setItem('ssc_user_answers', JSON.stringify(state.userAnswers));
    localStorage.setItem('ssc_submitted_states', JSON.stringify(state.submittedStates));
    localStorage.setItem('ssc_bookmarks', JSON.stringify(Array.from(state.bookmarks)));
  }

  function setupEventListeners() {
    DOM.themeToggleBtn.addEventListener('click', toggleTheme);
    DOM.resetStatsBtn.addEventListener('click', () => {
      if (confirm('Reset all answers and stats?')) {
        state.userAnswers = {};
        state.submittedStates = {};
        saveState();
        applyFilters();
        updateHeaderStats();
      }
    });

    DOM.openSearchBtn.addEventListener('click', () => {
      DOM.searchModal.classList.add('active');
      DOM.searchInput.focus();
    });

    DOM.closeSearchBtn.addEventListener('click', () => {
      DOM.searchModal.classList.remove('active');
    });

    DOM.searchInput.addEventListener('input', (e) => handleSearch(e.target.value));

    DOM.subjectFilterList.addEventListener('click', (e) => {
      const item = e.target.closest('.filter-item');
      if (!item) return;
      document.querySelectorAll('#subject-filter-list .filter-item').forEach(el => el.classList.remove('active'));
      item.classList.add('active');
      state.subjectFilter = item.dataset.subject;
      applyFilters();
    });

    DOM.btnBookmark.addEventListener('click', toggleBookmark);
    DOM.btnPrev.addEventListener('click', prevQ);
    DOM.btnNext.addEventListener('click', nextQ);
    DOM.btnSubmit.addEventListener('click', submitCurrentAnswer);
    DOM.btnToggleExplanation.addEventListener('click', () => {
      DOM.explanationBox.classList.toggle('visible');
    });
  }

  function prevQ() {
    if (state.currentIndex > 0) {
      state.currentIndex--;
      renderCurrentQuestion();
    }
  }

  function nextQ() {
    if (state.currentIndex < state.filteredQuestions.length - 1) {
      state.currentIndex++;
      renderCurrentQuestion();
    }
  }

  function applyFilters() {
    let list = state.allQuestions;
    if (state.subjectFilter !== 'all') {
      list = list.filter(q => q.subject === state.subjectFilter);
    }
    state.filteredQuestions = list;
    state.currentIndex = 0;
    renderQuestionGrid();
    renderCurrentQuestion();
  }

  function renderQuestionGrid() {
    DOM.gridLabel.textContent = `${state.filteredQuestions.length} Questions`;
    
    // For 10,000 items, render window around current index to maintain fast performance
    const total = state.filteredQuestions.length;
    const windowSize = 50;
    const startIdx = Math.max(0, state.currentIndex - 25);
    const endIdx = Math.min(total, startIdx + windowSize);

    let html = '';
    for (let idx = startIdx; idx < endIdx; idx++) {
      const q = state.filteredQuestions[idx];
      const isCurrent = idx === state.currentIndex;
      const isSubmitted = state.submittedStates[q.id];
      const isBookmarked = state.bookmarks.has(q.id);
      
      let statusClass = '';
      if (isSubmitted) {
        statusClass = (state.userAnswers[q.id] === q.correct_answer) ? 'correct' : 'incorrect';
      }

      if (isCurrent) statusClass += ' current';

      html += `<div class="nav-grid-item ${statusClass}" data-index="${idx}">${idx + 1}</div>`;
    }

    DOM.questionNavGrid.innerHTML = html;

    DOM.questionNavGrid.querySelectorAll('.nav-grid-item').forEach(item => {
      item.addEventListener('click', () => {
        state.currentIndex = parseInt(item.dataset.index, 10);
        renderCurrentQuestion();
      });
    });
  }

  function renderCurrentQuestion() {
    if (state.filteredQuestions.length === 0) return;
    const q = state.filteredQuestions[state.currentIndex];
    const isSubmitted = !!state.submittedStates[q.id];
    const userAns = state.userAnswers[q.id];

    DOM.qSubjectBadge.textContent = q.subject;
    DOM.qTopicBadge.textContent = q.topic;
    DOM.btnBookmark.textContent = state.bookmarks.has(q.id) ? '🔖' : '📑';

    DOM.qText.textContent = `Q${q.id}. ${q.question}`;

    let optionsHtml = '';
    const optionsObj = q.options || {};

    Object.keys(optionsObj).sort().forEach(key => {
      const optText = optionsObj[key];
      const isSelected = userAns === key;
      const isCorrectKey = q.correct_answer === key;

      let cardClass = 'option-card';
      if (isSelected) cardClass += ' selected';

      if (isSubmitted) {
        cardClass += ' disabled';
        if (isCorrectKey) {
          cardClass += ' correct';
        } else if (isSelected && !isCorrectKey) {
          cardClass += ' incorrect';
        }
      }

      optionsHtml += `
        <div class="${cardClass}" data-key="${key}">
          <div class="option-key">${key}</div>
          <div class="option-text">${optText}</div>
        </div>
      `;
    });

    DOM.qOptionsList.innerHTML = optionsHtml;

    if (!isSubmitted) {
      DOM.qOptionsList.querySelectorAll('.option-card').forEach(card => {
        card.addEventListener('click', () => {
          state.userAnswers[q.id] = card.dataset.key;
          saveState();
          renderCurrentQuestion();
        });
      });
    }

    DOM.btnSubmit.textContent = isSubmitted ? 'Answer Submitted ✓' : 'Submit Answer';
    DOM.btnSubmit.disabled = isSubmitted;

    if (isSubmitted) {
      DOM.explanationText.innerHTML = `<strong>Correct Answer: Option ${q.correct_answer}</strong><br><br>${q.explanation}`;
      DOM.explanationBox.classList.add('visible');
    } else {
      DOM.explanationBox.classList.remove('visible');
    }

    DOM.btnPrev.disabled = state.currentIndex === 0;
    DOM.btnNext.disabled = state.currentIndex === state.filteredQuestions.length - 1;

    renderQuestionGrid();
    updateHeaderStats();
  }

  function submitCurrentAnswer() {
    if (state.filteredQuestions.length === 0) return;
    const q = state.filteredQuestions[state.currentIndex];
    if (!state.userAnswers[q.id]) {
      alert('Please select an option first!');
      return;
    }
    state.submittedStates[q.id] = true;
    saveState();
    renderCurrentQuestion();
  }

  function toggleBookmark() {
    if (state.filteredQuestions.length === 0) return;
    const q = state.filteredQuestions[state.currentIndex];
    if (state.bookmarks.has(q.id)) {
      state.bookmarks.delete(q.id);
    } else {
      state.bookmarks.add(q.id);
    }
    saveState();
    renderCurrentQuestion();
  }

  function updateHeaderStats() {
    const answeredKeys = Object.keys(state.submittedStates);
    const totalAnswered = answeredKeys.length;
    let correctCount = 0;
    answeredKeys.forEach(id => {
      const q = state.allQuestions.find(item => item.id == id);
      if (q && state.userAnswers[id] === q.correct_answer) {
        correctCount++;
      }
    });

    const accuracy = totalAnswered > 0 ? Math.round((correctCount / totalAnswered) * 100) : 0;

    DOM.statAnswered.textContent = `${totalAnswered} / ${state.allQuestions.length}`;
    DOM.statAccuracy.textContent = `${accuracy}%`;
    DOM.statBookmarks.textContent = state.bookmarks.size;
  }

  function handleSearch(query) {
    if (!query || query.trim().length < 2) {
      DOM.searchResultsList.innerHTML = '<div style="color:var(--text-dark-muted); padding:1rem; text-align:center;">Type at least 2 characters...</div>';
      return;
    }
    const qLower = query.toLowerCase();
    const matches = state.allQuestions.filter(q => 
      q.question.toLowerCase().includes(qLower) || 
      q.topic.toLowerCase().includes(qLower) ||
      q.explanation.toLowerCase().includes(qLower)
    ).slice(0, 30);

    if (matches.length === 0) {
      DOM.searchResultsList.innerHTML = '<div style="color:var(--text-dark-muted); padding:1rem; text-align:center;">No matching questions.</div>';
      return;
    }

    let html = '';
    matches.forEach(q => {
      html += `
        <div class="search-result-item" data-qid="${q.id}">
          <div style="font-weight:700; color:var(--ssc-blue); font-size:0.85rem;">Q${q.id} • ${q.subject} • ${q.topic}</div>
          <div style="font-size:0.9rem;">${q.question}</div>
        </div>
      `;
    });
    DOM.searchResultsList.innerHTML = html;

    DOM.searchResultsList.querySelectorAll('.search-result-item').forEach(item => {
      item.addEventListener('click', () => {
        const qid = parseInt(item.dataset.qid, 10);
        DOM.searchModal.classList.remove('active');
        state.subjectFilter = 'all';
        state.filteredQuestions = state.allQuestions;
        const targetIdx = state.filteredQuestions.findIndex(q => q.id === qid);
        if (targetIdx !== -1) {
          state.currentIndex = targetIdx;
          renderCurrentQuestion();
        }
      });
    });
  }

  document.addEventListener('DOMContentLoaded', init);
})();
