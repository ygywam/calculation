import os
from generate_common import get_header, get_footer

def create_unit_1():
    title = "Ⅰ. 함수의 극한과 연속 - 01. 함수의 극한"
    page = "12 ~ 20쪽"
    filename = "1. 함수의 극한과 연속 1. 함수의 극한.html"
    
    body = f"""
    <!-- Mobile Top Header -->
    <header class="lg:hidden fixed top-0 left-0 right-0 h-16 bg-white/95 dark:bg-slate-800/95 backdrop-blur border-b border-slate-200 dark:border-slate-700 z-40 flex items-center justify-between px-4">
        <span class="font-bold text-lg text-indigo-600 dark:text-indigo-400">01. 함수의 극한</span>
        <button onclick="toggleWhiteboard()" class="px-2.5 py-1.5 rounded-lg bg-indigo-600 text-white text-xs font-bold flex items-center gap-1">
            <i class="fa-solid fa-chalkboard-user"></i> 칠판
        </button>
    </header>

    <!-- Sidebar -->
    <aside id="sidebar" class="fixed top-0 left-0 bottom-0 w-72 bg-white dark:bg-slate-800 border-r border-slate-200 dark:border-slate-700 z-40 flex flex-col justify-between shadow-lg lg:shadow-none">
        <div class="p-5 border-b border-slate-200 dark:border-slate-700">
            <span class="text-xs font-extrabold tracking-wider uppercase px-2.5 py-1 rounded-md bg-indigo-100 text-indigo-700 dark:bg-indigo-900 dark:text-indigo-300">Ⅰ. 함수의 극한과 연속</span>
            <h1 class="text-2xl font-extrabold text-slate-900 dark:text-white mt-2 flex items-center gap-2">
                <i class="fa-solid fa-chart-line text-indigo-600 dark:text-indigo-400"></i>
                <span>01. 함수의 극한</span>
            </h1>
            <p class="text-xs text-slate-500 dark:text-slate-400 mt-1">교과서 {page}</p>
        </div>
        <nav class="flex-1 overflow-y-auto py-3 px-2 space-y-1">
            <a href="#sec-intro" class="nav-link active flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700/50">
                <i class="fa-solid fa-lightbulb text-amber-500"></i><span>성취기준 & 생각 열기</span>
            </a>
            <a href="#sec-concept1" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700/50">
                <i class="fa-solid fa-arrow-right-to-bracket text-indigo-500"></i><span>1. 함수의 수렴과 발산</span>
            </a>
            <a href="#sec-concept2" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700/50">
                <i class="fa-solid fa-arrows-split-up-and-left text-emerald-500"></i><span>2. 좌극한과 우극한</span>
            </a>
            <a href="#sec-lab" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700/50">
                <i class="fa-solid fa-sliders text-sky-500"></i><span>인터랙티브 극한 탐구실</span>
            </a>
            <a href="#sec-ex1" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700/50">
                <i class="fa-solid fa-pen-to-square text-rose-500"></i><span>예제 & 문제 풀이</span>
            </a>
            <a href="#sec-check" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700/50">
                <i class="fa-solid fa-clipboard-check text-teal-500"></i><span>스스로 확인하기 (01~05)</span>
            </a>
            <a href="#sec-expand" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700/50">
                <i class="fa-solid fa-film text-purple-500"></i><span>수학과 미래 : CG 영상</span>
            </a>
        </nav>
        <div class="p-3 border-t border-slate-200 dark:border-slate-700 bg-slate-50/50 dark:bg-slate-800/50 no-print">
            <button onclick="toggleWhiteboard()" class="w-full py-2 px-3 rounded-xl bg-gradient-to-r from-indigo-600 to-sky-600 hover:from-indigo-500 hover:to-sky-500 text-white text-xs font-extrabold shadow-sm flex items-center justify-center gap-2 transition cursor-pointer">
                <i class="fa-solid fa-chalkboard-user"></i>
                <span>전자칠판 판서 모드</span>
            </button>
        </div>
    </aside>

    <!-- Main Content -->
    <main id="main-content" class="lg:ml-72 min-h-screen p-6 sm:p-10 space-y-12">
        <!-- Section Intro -->
        <section id="sec-intro" class="bg-white dark:bg-slate-800 rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 dark:border-slate-700">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-50 text-indigo-700 dark:bg-indigo-900/50 dark:text-indigo-300 text-xs font-bold mb-4">
                <i class="fa-solid fa-compass"></i> 성취기준
            </div>
            <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white mb-4">
                함수의 수렴과 발산의 뜻을 알고, 극한값을 구할 수 있다
            </h2>
            <div class="bg-indigo-50/70 dark:bg-slate-700/50 rounded-xl p-5 border border-indigo-100 dark:border-slate-600">
                <h3 class="font-bold text-indigo-900 dark:text-indigo-200 text-base mb-2">💡 생각 열기 : 분수함수의 구멍 난 곳에서의 함숫값?</h3>
                <p class="text-sm text-slate-700 dark:text-slate-300 leading-relaxed">
                    함수 $f(x) = \\frac{{x^2-1}}{{x-1}}$은 $x=1$에서 정의되지 않습니다. 하지만 $x$가 $1$에 한없이 가까워질 때, $f(x) = x+1$의 값은 어떤 수에 한없이 가까워질까요?
                </p>
                <div class="mt-3 flex items-center gap-3">
                    <button onclick="toggleSolution('intro-ans')" class="text-xs font-bold text-indigo-600 hover:underline">정답 확인</button>
                    <span id="intro-ans" class="hidden text-xs font-bold text-emerald-600">$x \\to 1$일 때 $f(x) \\to 2$로 한없이 가까워집니다 (수렴).</span>
                </div>
            </div>
        </section>

        <!-- Section Concept 1 -->
        <section id="sec-concept1" class="bg-white dark:bg-slate-800 rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 dark:border-slate-700 space-y-6">
            <div class="flex items-center gap-2.5 pb-3 border-b border-slate-200 dark:border-slate-700">
                <span class="w-2.5 h-6 bg-indigo-600 rounded-full"></span>
                <h3 class="text-xl font-bold text-slate-900 dark:text-white">1. 함수의 수렴과 극한값</h3>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="p-5 rounded-xl bg-slate-50 dark:bg-slate-700/40 border border-slate-200 dark:border-slate-600">
                    <h4 class="font-bold text-indigo-600 dark:text-indigo-400 mb-2">수렴 (Convergence)</h4>
                    <p class="text-sm text-slate-600 dark:text-slate-300 leading-relaxed">
                        함수 $f(x)$에서 $x$의 값이 $a$가 아니면서 $a$에 한없이 가까워질 때, $f(x)$의 값이 일정한 실수 $L$에 한없이 가까워지면 함수 $f(x)$는 <b>$L$에 수렴한다</b>고 합니다.
                    </p>
                    <div class="mt-3 p-3 bg-white dark:bg-slate-800 rounded-lg text-center font-bold text-indigo-600 dark:text-indigo-300">
                        $$\\lim_{{x \\to a}} f(x) = L \\quad \\text{{또는}} \\quad f(x) \\to L \\; (x \\to a)$$
                    </div>
                </div>
                <div class="p-5 rounded-xl bg-slate-50 dark:bg-slate-700/40 border border-slate-200 dark:border-slate-600">
                    <h4 class="font-bold text-rose-600 dark:text-rose-400 mb-2">발산 (Divergence)</h4>
                    <p class="text-sm text-slate-600 dark:text-slate-300 leading-relaxed">
                        함수 $f(x)$에서 $x \\to a$일 때 함숫값이 한없이 커지면 <b>양의 무한대로 발산</b>($+\\infty$), 한없이 작아지면 <b>음의 무한대로 발산</b>($-\\infty$)한다고 합니다.
                    </p>
                    <div class="mt-3 p-3 bg-white dark:bg-slate-800 rounded-lg text-center font-bold text-rose-600 dark:text-rose-300">
                        $$\\lim_{{x \\to a}} f(x) = \\infty \\quad \\text{{또는}} \\quad \\lim_{{x \\to a}} f(x) = -\\infty$$
                    </div>
                </div>
            </div>
        </section>

        <!-- Section Concept 2 -->
        <section id="sec-concept2" class="bg-white dark:bg-slate-800 rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 dark:border-slate-700 space-y-6">
            <div class="flex items-center gap-2.5 pb-3 border-b border-slate-200 dark:border-slate-700">
                <span class="w-2.5 h-6 bg-emerald-600 rounded-full"></span>
                <h3 class="text-xl font-bold text-slate-900 dark:text-white">2. 좌극한과 우극한, 그리고 극한의 존재 조건</h3>
            </div>
            <div class="p-5 rounded-xl bg-emerald-50/50 dark:bg-slate-700/40 border border-emerald-100 dark:border-slate-600">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <h4 class="font-bold text-emerald-800 dark:text-emerald-300 text-sm mb-1">우극한 (Right-hand Limit)</h4>
                        <p class="text-xs text-slate-600 dark:text-slate-300 mb-2">$x$가 $a$보다 크면서 $a$에 접근할 때</p>
                        <p class="font-bold text-emerald-600 dark:text-emerald-400">$$\\lim_{{x \\to a^+}} f(x)$$</p>
                    </div>
                    <div>
                        <h4 class="font-bold text-emerald-800 dark:text-emerald-300 text-sm mb-1">좌극한 (Left-hand Limit)</h4>
                        <p class="text-xs text-slate-600 dark:text-slate-300 mb-2">$x$가 $a$보다 작으면서 $a$에 접근할 때</p>
                        <p class="font-bold text-emerald-600 dark:text-emerald-400">$$\\lim_{{x \\to a^-}} f(x)$$</p>
                    </div>
                </div>
                <div class="mt-4 p-4 rounded-xl bg-white dark:bg-slate-800 border border-emerald-200 dark:border-slate-600 text-center">
                    <p class="text-sm font-extrabold text-slate-800 dark:text-slate-100">⭐ 함수의 극한의 존재 필요충분조건</p>
                    <p class="text-base font-black text-indigo-600 dark:text-indigo-400 mt-1">
                        $$\\lim_{{x \\to a}} f(x) = L \\iff \\lim_{{x \\to a^+}} f(x) = \\lim_{{x \\to a^-}} f(x) = L$$
                    </p>
                </div>
            </div>
        </section>

        <!-- Section Interactive Lab -->
        <section id="sec-lab" class="bg-white dark:bg-slate-800 rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 dark:border-slate-700 space-y-6">
            <div class="flex items-center justify-between pb-3 border-b border-slate-200 dark:border-slate-700">
                <div class="flex items-center gap-2.5">
                    <span class="w-2.5 h-6 bg-sky-600 rounded-full"></span>
                    <h3 class="text-xl font-bold text-slate-900 dark:text-white">인터랙티브 극한 시각화 실험실</h3>
                </div>
                <span class="text-xs font-bold text-sky-600 dark:text-sky-400 bg-sky-50 dark:bg-sky-900/50 px-2.5 py-1 rounded-full">좌/우 극한 탐구</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-center">
                <div class="md:col-span-2 bg-slate-900 rounded-xl p-4 flex flex-col items-center">
                    <canvas id="limit-canvas" width="500" height="260" class="w-full h-56 rounded-lg"></canvas>
                </div>
                <div class="space-y-4">
                    <div>
                        <label class="block text-xs font-bold text-slate-500 mb-1">접근할 목표점 $a = 1$로 $x$ 이동</label>
                        <input type="range" id="x-slider" min="0" max="2" step="0.05" value="0.4" class="w-full accent-indigo-600 cursor-pointer">
                        <div class="flex justify-between text-xs text-slate-400 mt-1">
                            <span>$x = 0$ (좌)</span>
                            <span id="x-val" class="font-bold text-indigo-600 text-sm">x = 0.40</span>
                            <span>$x = 2$ (우)</span>
                        </div>
                    </div>
                    <div class="p-3 bg-slate-50 dark:bg-slate-700/50 rounded-xl space-y-2 text-xs">
                        <div class="flex justify-between">
                            <span class="text-slate-500">함수식:</span>
                            <span class="font-bold">$f(x) = 2x + 1$</span>
                        </div>
                        <div class="flex justify-between">
                            <span class="text-slate-500">현재 함숫값:</span>
                            <span id="fx-val" class="font-black text-indigo-600 text-sm">f(x) = 1.80</span>
                        </div>
                        <div class="flex justify-between border-t border-slate-200 dark:border-slate-600 pt-2">
                            <span class="text-slate-500">목표 극한값:</span>
                            <span class="font-black text-emerald-600 text-sm">L = 3.00</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Section Examples & Problems -->
        <section id="sec-ex1" class="bg-white dark:bg-slate-800 rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 dark:border-slate-700 space-y-6">
            <div class="flex items-center gap-2.5 pb-3 border-b border-slate-200 dark:border-slate-700">
                <span class="w-2.5 h-6 bg-rose-600 rounded-full"></span>
                <h3 class="text-xl font-bold text-slate-900 dark:text-white">교과서 대표 예제 & 연습장</h3>
            </div>
            <div class="p-5 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50/50 dark:bg-slate-700/30 space-y-3">
                <div class="flex items-center justify-between">
                    <span class="px-2.5 py-1 rounded bg-rose-100 text-rose-700 dark:bg-rose-900/50 dark:text-rose-300 text-xs font-bold">예제 1</span>
                    <button onclick="toggleSolution('sol-ex1')" class="text-xs font-bold text-indigo-600 dark:text-indigo-400 hover:underline">풀이 열기/닫기</button>
                </div>
                <h4 class="font-bold text-slate-900 dark:text-white text-base">
                    함수 $f(x) = \\frac{{|x-1|}}{{x-1}}$에 대하여 $\\lim_{{x \\to 1}} f(x)$가 존재하는지 조사하시오.
                </h4>
                <div id="sol-ex1" class="hidden p-4 rounded-xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-600 text-sm space-y-2">
                    <p>• 우극한 : $x > 1$일 때 $|x-1| = x-1$이므로 $\\lim_{{x \\to 1^+}} \\frac{{x-1}}{{x-1}} = 1$</p>
                    <p>• 좌극한 : $x < 1$일 때 $|x-1| = -(x-1)$이므로 $\\lim_{{x \\to 1^-}} \\frac{{-(x-1)}}{{x-1}} = -1$</p>
                    <p class="font-bold text-rose-600">우극한($1$)과 좌극한($-1$)이 서로 다르므로 극한값은 존재하지 않는다.</p>
                </div>
                <!-- Scratchpad Canvas -->
                <div class="mt-4">
                    <div class="flex justify-between items-center mb-1.5 text-xs text-slate-400">
                        <span><i class="fa-solid fa-pen-nib mr-1"></i> 문제 풀이 연습장</span>
                        <button class="clear-scratchpad-btn hover:text-slate-600 dark:hover:text-slate-200 font-bold">지우기</button>
                    </div>
                    <canvas class="scratchpad-canvas w-full h-36 rounded-xl border border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-900"></canvas>
                </div>
            </div>
        </section>

        <!-- Section Self Check -->
        <section id="sec-check" class="bg-white dark:bg-slate-800 rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 dark:border-slate-700 space-y-6">
            <div class="flex items-center gap-2.5 pb-3 border-b border-slate-200 dark:border-slate-700">
                <span class="w-2.5 h-6 bg-teal-600 rounded-full"></span>
                <h3 class="text-xl font-bold text-slate-900 dark:text-white">스스로 확인하기 (형성평가)</h3>
            </div>
            <div class="space-y-4">
                <div class="p-4 rounded-xl bg-slate-50 dark:bg-slate-700/40 border border-slate-200 dark:border-slate-600">
                    <p class="font-bold text-sm mb-2">01. 극한값 $\\lim_{{x \\to 2}} (x^2 - 3x + 4)$의 값은?</p>
                    <div class="flex items-center gap-2">
                        <button onclick="toggleSolution('ans-01')" class="px-3 py-1 bg-teal-600 hover:bg-teal-700 text-white rounded-lg text-xs font-bold transition">정답 확인</button>
                        <span id="ans-01" class="hidden font-bold text-sm text-teal-600">$2^2 - 3(2) + 4 = 2$</span>
                    </div>
                </div>
                <div class="p-4 rounded-xl bg-slate-50 dark:bg-slate-700/40 border border-slate-200 dark:border-slate-600">
                    <p class="font-bold text-sm mb-2">02. [OX] 우극한과 좌극한이 모두 존재하면 극한값은 반드시 존재한다. (O/X)</p>
                    <div class="flex items-center gap-2">
                        <button onclick="toggleSolution('ans-02')" class="px-3 py-1 bg-teal-600 hover:bg-teal-700 text-white rounded-lg text-xs font-bold transition">정답 확인</button>
                        <span id="ans-02" class="hidden font-bold text-sm text-rose-600">X (두 극한값이 '서로 같아야' 존재합니다)</span>
                    </div>
                </div>
                <div class="p-4 rounded-xl bg-slate-50 dark:bg-slate-700/40 border border-slate-200 dark:border-slate-600">
                    <p class="font-bold text-sm mb-2">03. 극한값 $\\lim_{{x \\to \\infty}} \\frac{{1}}{{x}}$의 값은?</p>
                    <div class="flex items-center gap-2">
                        <button onclick="toggleSolution('ans-03')" class="px-3 py-1 bg-teal-600 hover:bg-teal-700 text-white rounded-lg text-xs font-bold transition">정답 확인</button>
                        <span id="ans-03" class="hidden font-bold text-sm text-teal-600">$0$</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- Section Expand / Career -->
        <section id="sec-expand" class="bg-gradient-to-r from-purple-50 to-indigo-50 dark:from-slate-800 dark:to-slate-800 rounded-2xl p-6 sm:p-8 border border-purple-100 dark:border-slate-700">
            <div class="flex items-center gap-3 mb-3">
                <i class="fa-solid fa-wand-magic-sparkles text-2xl text-purple-600 dark:text-purple-400"></i>
                <h3 class="text-xl font-bold text-slate-900 dark:text-white">수학으로 꿈꾸는 미래 : CG와 모션 그래픽스</h3>
            </div>
            <p class="text-sm text-slate-600 dark:text-slate-300 leading-relaxed">
                컴퓨터 그래픽에서 부드러운 카메라 무빙과 캐릭터의 연속적인 움직임을 표현할 때, 이산적인 키프레임 사이를 보간(Interpolation)하는 곡선의 극한 이론이 핵심 알고리즘으로 활용됩니다.
            </p>
        </section>
    </main>

    <!-- Interactive Canvas Script -->
    <script>
    const cv = document.getElementById('limit-canvas');
    if (cv) {{
        const ctx = cv.getContext('2d');
        const slider = document.getElementById('x-slider');
        const xVal = document.getElementById('x-val');
        const fxVal = document.getElementById('fx-val');

        function draw() {{
            const x = parseFloat(slider.value);
            const fx = 2 * x + 1;
            xVal.textContent = 'x = ' + x.toFixed(2);
            fxVal.textContent = 'f(x) = ' + fx.toFixed(2);

            ctx.clearRect(0, 0, cv.width, cv.height);

            // Coordinates
            const originX = 60;
            const originY = 220;
            const scaleX = 180;
            const scaleY = 40;

            // Axes
            ctx.strokeStyle = '#475569';
            ctx.lineWidth = 1.5;
            ctx.beginPath();
            ctx.moveTo(30, originY);
            ctx.lineTo(460, originY);
            ctx.moveTo(originX, 20);
            ctx.lineTo(originX, 240);
            ctx.stroke();

            // Function Line y = 2x + 1
            ctx.strokeStyle = '#6366f1';
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.moveTo(originX + 0 * scaleX, originY - 1 * scaleY);
            ctx.lineTo(originX + 2.2 * scaleX, originY - 5.4 * scaleY);
            ctx.stroke();

            // Target Point (1, 3)
            ctx.fillStyle = '#10b981';
            ctx.beginPath();
            ctx.arc(originX + 1 * scaleX, originY - 3 * scaleY, 6, 0, Math.PI * 2);
            ctx.fill();

            // Moving Point (x, fx)
            ctx.fillStyle = '#ef4444';
            ctx.beginPath();
            ctx.arc(originX + x * scaleX, originY - fx * scaleY, 7, 0, Math.PI * 2);
            ctx.fill();

            // Guideline
            ctx.setLineDash([4, 4]);
            ctx.strokeStyle = '#94a3b8';
            ctx.beginPath();
            ctx.moveTo(originX + x * scaleX, originY);
            ctx.lineTo(originX + x * scaleX, originY - fx * scaleY);
            ctx.lineTo(originX, originY - fx * scaleY);
            ctx.stroke();
            ctx.setLineDash([]);
        }}
        slider.addEventListener('input', draw);
        draw();
    }}
    </script>
    """
    
    html = get_header(title, page) + body + get_footer()
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Created:", filename)

if __name__ == '__main__':
    create_unit_1()
