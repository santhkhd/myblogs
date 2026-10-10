"""
Daily 50-Question GK & Current Affairs Quiz Publisher
Generates interactive, responsive, self-contained Blogger Quiz Post HTML & XML
"""

import os
import json
import datetime
from quiz_generator import get_daily_50_quiz, CATEGORIES

def build_daily_quiz_html(date_str=None):
    if not date_str:
        date_str = datetime.date.today().strftime("%d %B %Y")
    
    questions = get_daily_50_quiz(date_str)
    questions_json = json.dumps(questions, ensure_ascii=False)

    html = f"""<!-- Daily 50-Question Interactive GK & Current Affairs Mock Test -->
<div id="quizAppContainer" style="font-family:'Plus Jakarta Sans',sans-serif; max-width:860px; margin:0 auto; color:#0F172A;">
  <style>
    .quiz-hero-banner {{
      background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%);
      color: #FFFFFF;
      padding: 1.75rem;
      border-radius: 14px;
      text-align: center;
      margin-bottom: 1.5rem;
      box-shadow: 0 10px 25px -5px rgba(37,99,235,0.25);
    }}
    .quiz-stats-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #FFFFFF;
      border: 1.5px solid #E2E8F0;
      padding: 12px 18px;
      border-radius: 12px;
      margin-bottom: 1.5rem;
      font-weight: 700;
      font-size: 0.9rem;
      flex-wrap: wrap;
      gap: 10px;
    }}
    .quiz-card {{
      background: #FFFFFF;
      border: 1.5px solid #E2E8F0;
      border-radius: 14px;
      padding: 1.75rem;
      box-shadow: 0 2px 8px rgba(0,0,0,0.04);
      margin-bottom: 1.5rem;
    }}
    .quiz-cat-badge {{
      display: inline-block;
      background: #EFF6FF;
      color: #2563EB;
      padding: 4px 12px;
      border-radius: 50px;
      font-size: 0.78rem;
      font-weight: 800;
      margin-bottom: 10px;
      text-transform: uppercase;
    }}
    .quiz-q-title {{
      font-size: 1.15rem;
      font-weight: 800;
      line-height: 1.5;
      margin-bottom: 1.25rem;
      color: #0F172A;
    }}
    .quiz-options-list {{
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}
    .quiz-opt-btn {{
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 12px 16px;
      border: 1.5px solid #E2E8F0;
      background: #F8FAFC;
      border-radius: 10px;
      font-size: 0.95rem;
      font-weight: 600;
      cursor: pointer;
      text-align: left;
      transition: all 0.2s ease;
      width: 100%;
    }}
    .quiz-opt-btn:hover:not(:disabled) {{
      background: #EFF6FF;
      border-color: #2563EB;
      transform: translateX(3px);
    }}
    .quiz-opt-btn.correct {{
      background: #ECFDF5 !important;
      border-color: #059669 !important;
      color: #065F46 !important;
    }}
    .quiz-opt-btn.wrong {{
      background: #FEE2E2 !important;
      border-color: #DC2626 !important;
      color: #991B1B !important;
    }}
    .opt-letter {{
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: #E2E8F0;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 0.8rem;
      flex-shrink: 0;
    }}
    .quiz-opt-btn.correct .opt-letter {{
      background: #059669;
      color: #FFFFFF;
    }}
    .quiz-opt-btn.wrong .opt-letter {{
      background: #DC2626;
      color: #FFFFFF;
    }}
    .quiz-exp-box {{
      background: #F0FDF4;
      border-left: 4px solid #059669;
      padding: 12px 16px;
      border-radius: 8px;
      margin-top: 1.25rem;
      font-size: 0.88rem;
      line-height: 1.6;
      color: #166534;
      display: none;
    }}
    .quiz-nav-btns {{
      display: flex;
      justify-content: space-between;
      margin-top: 1.5rem;
      gap: 10px;
    }}
    .q-btn-action {{
      padding: 10px 20px;
      border-radius: 8px;
      font-weight: 800;
      font-size: 0.9rem;
      border: none;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .q-btn-prev {{ background: #E2E8F0; color: #475569; }}
    .q-btn-next {{ background: #2563EB; color: #FFFFFF; }}
    .q-btn-submit {{ background: #059669; color: #FFFFFF; }}
    
    .q-palette-grid {{
      display: grid;
      grid-template-columns: repeat(10, 1fr);
      gap: 6px;
      margin-top: 1.5rem;
      background: #FFFFFF;
      padding: 14px;
      border-radius: 12px;
      border: 1px solid #E2E8F0;
    }}
    @media (max-width: 600px) {{
      .q-palette-grid {{ grid-template-columns: repeat(5, 1fr); }}
    }}
    .q-num-btn {{
      padding: 8px 0;
      font-size: 0.82rem;
      font-weight: 800;
      border-radius: 6px;
      border: 1px solid #CBD5E1;
      background: #F8FAFC;
      cursor: pointer;
      text-align: center;
    }}
    .q-num-btn.active {{ border-color: #2563EB; background: #2563EB; color: #FFF; }}
    .q-num-btn.answered {{ border-color: #059669; background: #ECFDF5; color: #059669; }}

    .quiz-result-scorecard {{
      background: #FFFFFF;
      border: 2px solid #059669;
      border-radius: 16px;
      padding: 2.25rem;
      text-align: center;
      display: none;
      box-shadow: 0 10px 30px rgba(5,150,105,0.15);
    }}
  </style>

  <div class="quiz-hero-banner">
    <div style="font-size:0.8rem; font-weight:800; letter-spacing:1px; opacity:0.9; text-transform:uppercase;">🏆 Daily Exam Practice Suite</div>
    <h1 style="font-size:1.6rem; font-weight:900; margin:6px 0 8px; color:#FFFFFF;">GK &amp; Current Affairs 50-Question Mock Test</h1>
    <p style="margin:0; font-size:0.9rem; opacity:0.92;">Daily Practice Set for Kerala PSC, SSC CGL, RRB NTPC, Banking &amp; UPSC | {date_str}</p>
  </div>

  <div class="quiz-stats-bar">
    <div>⏳ Time Left: <span id="quizTimerDisplay" style="color:#DC2626; font-size:1rem; font-weight:900;">30:00</span></div>
    <div>📊 Question: <span id="qCurrentIndex">1</span> of <span id="qTotalCount">50</span></div>
    <div>🎯 Score: <span id="qLiveScore" style="color:#059669;">0</span></div>
  </div>

  <!-- Active Question Card -->
  <div id="activeQuizCardWrapper">
    <div class="quiz-card">
      <span class="quiz-cat-badge" id="qCategoryBadge">Category</span>
      <div class="quiz-q-title" id="qQuestionText">Loading Question...</div>
      <div class="quiz-options-list" id="qOptionsList"></div>
      <div class="quiz-exp-box" id="qExplanationBox"></div>

      <div class="quiz-nav-btns">
        <button class="q-btn-action q-btn-prev" onclick="goToPrevQ()" id="btnPrevQ" type="button">◀ Previous</button>
        <button class="q-btn-action q-btn-next" onclick="goToNextQ()" id="btnNextQ" type="button">Next Question ▶</button>
        <button class="q-btn-action q-btn-submit" onclick="submitQuiz()" id="btnSubmitQuiz" style="display:none;" type="button">Submit Test ➔</button>
      </div>
    </div>

    <!-- Number Palette Grid -->
    <div style="font-size:0.85rem; font-weight:800; margin-bottom:6px; color:#475569;">Question Navigation Palette:</div>
    <div class="q-palette-grid" id="qPaletteGrid"></div>
  </div>

  <!-- Scorecard / Result Section -->
  <div class="quiz-result-scorecard" id="quizScorecard">
    <div style="font-size:3rem; margin-bottom:0.5rem;">🎉</div>
    <h2 style="font-size:1.6rem; font-weight:900; color:#0F172A; margin-bottom:0.5rem;">Mock Test Completed!</h2>
    <p style="color:#64748B; margin-bottom:1.5rem;">Official Result Summary for {date_str}</p>

    <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:12px; max-width:500px; margin:0 auto 1.75rem;">
      <div style="background:#ECFDF5; padding:12px; border-radius:10px; border:1px solid #A7F3D0;">
        <div style="font-size:0.8rem; color:#065F46; font-weight:700;">Score</div>
        <div id="finalScoreVal" style="font-size:1.5rem; font-weight:900; color:#059669;">0 / 50</div>
      </div>
      <div style="background:#EFF6FF; padding:12px; border-radius:10px; border:1px solid #BFDBFE;">
        <div style="font-size:0.8rem; color:#1E40AF; font-weight:700;">Accuracy</div>
        <div id="finalAccuracyVal" style="font-size:1.5rem; font-weight:900; color:#2563EB;">0%</div>
      </div>
      <div style="background:#FEF3C7; padding:12px; border-radius:10px; border:1px solid #FDE68A;">
        <div style="font-size:0.8rem; color:#92400E; font-weight:700;">Attempted</div>
        <div id="finalAttemptedVal" style="font-size:1.5rem; font-weight:900; color:#D97706;">0 / 50</div>
      </div>
    </div>

    <button onclick="restartQuiz()" class="q-btn-action q-btn-next" style="padding:12px 28px; font-size:1rem;" type="button">🔄 Retake Practice Test</button>
  </div>

  <!-- Quiz Engine Logic -->
  <script type="text/javascript">
    (function() {{
      var QUIZ_QUESTIONS = {questions_json};
      var currentQIdx = 0;
      var userAnswers = new Array(QUIZ_QUESTIONS.length).fill(null);
      var timeLeft = 30 * 60; // 30 minutes
      var timerInterval = null;

      function startTimer() {{
        timerInterval = setInterval(function() {{
          timeLeft--;
          if (timeLeft <= 0) {{
            clearInterval(timerInterval);
            submitQuiz();
            return;
          }}
          var mins = Math.floor(timeLeft / 60);
          var secs = timeLeft % 60;
          var disp = document.getElementById('quizTimerDisplay');
          if (disp) {{
            disp.innerText = (mins < 10 ? '0' : '') + mins + ':' + (secs < 10 ? '0' : '') + secs;
          }}
        }}, 1000);
      }}

      function renderQuestion(idx) {{
        currentQIdx = idx;
        var q = QUIZ_QUESTIONS[idx];
        document.getElementById('qCurrentIndex').innerText = (idx + 1);
        document.getElementById('qCategoryBadge').innerText = q.category || 'General Knowledge';
        document.getElementById('qQuestionText').innerText = (idx + 1) + '. ' + q.question;

        var optContainer = document.getElementById('qOptionsList');
        optContainer.innerHTML = '';
        var letters = ['A', 'B', 'C', 'D'];

        for (var i = 0; i < q.options.length; i++) {{
          var btn = document.createElement('button');
          btn.className = 'quiz-opt-btn';
          btn.type = 'button';
          btn.dataset.optidx = i;
          
          if (userAnswers[idx] !== null) {{
            btn.disabled = true;
            if (i === q.correct_index) btn.classList.add('correct');
            else if (i === userAnswers[idx]) btn.classList.add('wrong');
          }}

          btn.innerHTML = "<span class='opt-letter'>" + letters[i] + "</span><span>" + q.options[i] + "</span>";
          btn.onclick = function() {{
            var chosen = parseInt(this.dataset.optidx, 10);
            selectAnswer(chosen);
          }};
          optContainer.appendChild(btn);
        }}

        var expBox = document.getElementById('qExplanationBox');
        if (userAnswers[idx] !== null) {{
          expBox.style.display = 'block';
          expBox.innerHTML = "💡 <strong>Explanation &amp; Exam Facts:</strong> " + q.explanation;
        }} else {{
          expBox.style.display = 'none';
        }}

        document.getElementById('btnPrevQ').style.visibility = (idx === 0 ? 'hidden' : 'visible');
        if (idx === QUIZ_QUESTIONS.length - 1) {{
          document.getElementById('btnNextQ').style.display = 'none';
          document.getElementById('btnSubmitQuiz').style.display = 'inline-block';
        }} else {{
          document.getElementById('btnNextQ').style.display = 'inline-block';
          document.getElementById('btnSubmitQuiz').style.display = 'none';
        }}

        renderPalette();
        updateScore();
      }}

      function selectAnswer(chosenIdx) {{
        if (userAnswers[currentQIdx] !== null) return;
        userAnswers[currentQIdx] = chosenIdx;
        renderQuestion(currentQIdx);
      }}

      function renderPalette() {{
        var pGrid = document.getElementById('qPaletteGrid');
        if (!pGrid) return;
        pGrid.innerHTML = '';
        for (var i = 0; i < QUIZ_QUESTIONS.length; i++) {{
          var btn = document.createElement('button');
          btn.className = 'q-num-btn';
          btn.type = 'button';
          btn.innerText = (i + 1);
          if (i === currentQIdx) btn.classList.add('active');
          if (userAnswers[i] !== null) btn.classList.add('answered');
          btn.onclick = (function(targetIdx) {{
            return function() {{ renderQuestion(targetIdx); }};
          }})(i);
          pGrid.appendChild(btn);
        }}
      }}

      function updateScore() {{
        var correct = 0;
        for (var i = 0; i < userAnswers.length; i++) {{
          if (userAnswers[i] === QUIZ_QUESTIONS[i].correct_index) correct++;
        }}
        var scoreEl = document.getElementById('qLiveScore');
        if (scoreEl) scoreEl.innerText = correct;
      }}

      window.goToNextQ = function() {{
        if (currentQIdx < QUIZ_QUESTIONS.length - 1) {{
          renderQuestion(currentQIdx + 1);
        }}
      }};

      window.goToPrevQ = function() {{
        if (currentQIdx > 0) {{
          renderQuestion(currentQIdx - 1);
        }}
      }};

      window.submitQuiz = function() {{
        clearInterval(timerInterval);
        var correct = 0;
        var attempted = 0;
        for (var i = 0; i < userAnswers.length; i++) {{
          if (userAnswers[i] !== null) {{
            attempted++;
            if (userAnswers[i] === QUIZ_QUESTIONS[i].correct_index) correct++;
          }}
        }}

        document.getElementById('activeQuizCardWrapper').style.display = 'none';
        var scorecard = document.getElementById('quizScorecard');
        scorecard.style.display = 'block';

        document.getElementById('finalScoreVal').innerText = correct + ' / ' + QUIZ_QUESTIONS.length;
        document.getElementById('finalAttemptedVal').innerText = attempted + ' / ' + QUIZ_QUESTIONS.length;
        var acc = attempted > 0 ? Math.round((correct / attempted) * 100) : 0;
        document.getElementById('finalAccuracyVal').innerText = acc + '%';
      }};

      window.restartQuiz = function() {{
        userAnswers = new Array(QUIZ_QUESTIONS.length).fill(null);
        timeLeft = 30 * 60;
        document.getElementById('quizScorecard').style.display = 'none';
        document.getElementById('activeQuizCardWrapper').style.display = 'block';
        startTimer();
        renderQuestion(0);
      }};

      document.getElementById('qTotalCount').innerText = QUIZ_QUESTIONS.length;
      startTimer();
      renderQuestion(0);
    }})();
  </script>
</div>
"""
    return html

def save_sample_daily_post():
    out_path = os.path.join(os.path.dirname(__file__), "daily_50_quiz_post.html")
    html_content = build_daily_quiz_html()
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print("SUCCESS: Generated 'daily_50_quiz_post.html' ready for Blogger posting!")

if __name__ == "__main__":
    save_sample_daily_post()
