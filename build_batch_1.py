import os
from generate_common import get_header, get_footer

def create_unit_3():
    title = "Ⅰ. 함수의 극한과 연속 - 03. 함수의 연속"
    page = "29 ~ 34쪽"
    filename = "1. 함수의 극한과 연속 3. 함수의 연속.html"

    body = f"""
    <header class="lg:hidden fixed top-0 left-0 right-0 h-16 bg-white/95 backdrop-blur border-b border-slate-200 z-40 flex items-center justify-between px-4">
        <span class="font-bold text-lg text-indigo-600">03. 함수의 연속</span>
        <button onclick="toggleWhiteboard()" class="px-2.5 py-1.5 rounded-lg bg-indigo-600 text-white text-xs font-bold flex items-center gap-1">
            <i class="fa-solid fa-chalkboard-user"></i> 칠판
        </button>
    </header>

    <aside id="sidebar" class="fixed top-0 left-0 bottom-0 w-72 bg-white border-r border-slate-200 z-40 flex flex-col justify-between shadow-lg lg:shadow-none">
        <div class="p-5 border-b border-slate-200">
            <span class="text-xs font-extrabold tracking-wider uppercase px-2.5 py-1 rounded-md bg-indigo-100 text-indigo-700">Ⅰ. 함수의 극한과 연속</span>
            <h1 class="text-2xl font-extrabold text-slate-900 mt-2 flex items-center gap-2">
                <i class="fa-solid fa-link text-indigo-600"></i>
                <span>03. 함수의 연속</span>
            </h1>
            <p class="text-xs text-slate-500 mt-1">교과서 {page}</p>
        </div>
        <nav class="flex-1 overflow-y-auto py-3 px-2 space-y-1">
            <a href="#sec-intro" class="nav-link active flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-lightbulb text-amber-500"></i><span>성취기준 & 생각 열기</span>
            </a>
            <a href="#sec-concept1" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-circle-check text-indigo-500"></i><span>1. 연속의 3가지 조건</span>
            </a>
            <a href="#sec-concept2" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-arrows-split-up-and-left text-emerald-500"></i><span>2. 불연속 유형과 구간</span>
            </a>
            <a href="#sec-lab" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-sliders text-sky-500"></i><span>연속/불연속 인터랙티브 실험</span>
            </a>
            <a href="#sec-ex1" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-pen-to-square text-rose-500"></i><span>대표 예제 & 연습장</span>
            </a>
            <a href="#sec-check" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-clipboard-check text-teal-500"></i><span>스스로 확인하기 (01~04)</span>
            </a>
        </nav>
        <div class="p-3 border-t border-slate-200 bg-slate-50 no-print">
            <button onclick="toggleWhiteboard()" class="w-full py-2 px-3 rounded-xl bg-gradient-to-r from-indigo-600 to-sky-600 hover:from-indigo-500 hover:to-sky-500 text-white text-xs font-extrabold shadow-sm flex items-center justify-center gap-2 transition cursor-pointer">
                <i class="fa-solid fa-chalkboard-user"></i>
                <span>전자칠판 판서 모드</span>
            </button>
        </div>
    </aside>

    <main id="main-content" class="lg:ml-72 min-h-screen p-6 sm:p-10 space-y-12">
        <section id="sec-intro" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-50 text-indigo-700 text-xs font-bold mb-4">
                <i class="fa-solid fa-compass"></i> 성취기준
            </div>
            <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 mb-4">
                함수의 연속의 뜻을 알고, 여러 가지 함수의 연속성을 판별할 수 있다
            </h2>
            <div class="bg-indigo-50/70 rounded-xl p-5 border border-indigo-100">
                <h3 class="font-bold text-indigo-900 text-base mb-2">💡 생각 열기 : 그래프가 '끊어지지 않는다'는 것의 수학적 의미?</h3>
                <p class="text-sm text-slate-700 leading-relaxed">
                    선이나 곡선이 중간에 끊어짐 없이 이어져 있다는 직관적 개념을 수학적으로 엄밀하게 정의하려면 어떻게 해야 할까요? 특정 점 $x=a$에서 함수가 연속이 되기 위한 조건을 살펴봅시다.
                </p>
                <div class="mt-3 flex items-center gap-3">
                    <button onclick="toggleSolution('intro-ans3')" class="text-xs font-bold text-indigo-600 hover:underline">정답 확인</button>
                    <span id="intro-ans3" class="hidden text-xs font-bold text-emerald-600">함숫값이 정의되고, 극한값이 존재하며, 그 두 값이 서로 일치해야 합니다!</span>
                </div>
            </div>
        </section>

        <section id="sec-concept1" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center gap-2.5 pb-3 border-b border-slate-200">
                <span class="w-2.5 h-6 bg-indigo-600 rounded-full"></span>
                <h3 class="text-xl font-bold text-slate-900">1. $x=a$에서 연속의 3가지 조건</h3>
            </div>
            <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-4">
                <p class="text-sm font-bold text-slate-800">함수 $f(x)$가 $x=a$에서 연속이 되기 위해서는 다음 3가지 조건을 <b>모두</b> 만족해야 합니다:</p>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-xs">
                        <div class="w-7 h-7 rounded-full bg-indigo-100 text-indigo-700 font-bold flex items-center justify-center text-xs mb-2">1</div>
                        <h4 class="font-bold text-slate-900 text-sm mb-1">함숫값의 존재</h4>
                        <p class="text-xs text-slate-600">$x=a$에서 함숫값 $f(a)$가 정의되어 있다.</p>
                    </div>
                    <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-xs">
                        <div class="w-7 h-7 rounded-full bg-indigo-100 text-indigo-700 font-bold flex items-center justify-center text-xs mb-2">2</div>
                        <h4 class="font-bold text-slate-900 text-sm mb-1">극한값의 존재</h4>
                        <p class="text-xs text-slate-600">극한값 $\\lim_{{x \\to a}} f(x)$가 존재한다.<br>(좌극한 = 우극한)</p>
                    </div>
                    <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-xs">
                        <div class="w-7 h-7 rounded-full bg-indigo-100 text-indigo-700 font-bold flex items-center justify-center text-xs mb-2">3</div>
                        <h4 class="font-bold text-slate-900 text-sm mb-1">두 값의 일치</h4>
                        <p class="text-xs text-slate-600">$$\\lim_{{x \\to a}} f(x) = f(a)$$</p>
                    </div>
                </div>
                <div class="p-3 rounded-lg bg-amber-50 border border-amber-200 text-xs text-amber-900 font-medium">
                    <i class="fa-solid fa-circle-exclamation mr-1 text-amber-600"></i>
                    셋 중 하나라도 만족하지 않으면 함수 $f(x)$는 $x=a$에서 <b>불연속</b>이라고 합니다.
                </div>
            </div>
        </section>

        <section id="sec-concept2" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center gap-2.5 pb-3 border-b border-slate-200">
                <span class="w-2.5 h-6 bg-emerald-600 rounded-full"></span>
                <h3 class="text-xl font-bold text-slate-900">2. 불연속의 대표 3가지 유형 & 구간 기호</h3>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
                    <span class="text-xs font-bold text-rose-600 bg-rose-50 px-2 py-0.5 rounded">유형 1</span>
                    <h4 class="font-bold text-slate-800 text-sm mt-2 mb-1">함숫값이 정의되지 않음</h4>
                    <p class="text-xs text-slate-600">예: $f(x) = \\frac{{x^2-1}}{{x-1}}$ ($x=1$에서 분모가 0이 되어 정의 안 됨)</p>
                </div>
                <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
                    <span class="text-xs font-bold text-rose-600 bg-rose-50 px-2 py-0.5 rounded">유형 2</span>
                    <h4 class="font-bold text-slate-800 text-sm mt-2 mb-1">극한값이 존재하지 않음</h4>
                    <p class="text-xs text-slate-600">예: 가우스 기호 $[x]$ 또는 좌극한 $\\ne$ 우극한인 계단형 조각함수</p>
                </div>
                <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
                    <span class="text-xs font-bold text-rose-600 bg-rose-50 px-2 py-0.5 rounded">유형 3</span>
                    <h4 class="font-bold text-slate-800 text-sm mt-2 mb-1">극한값 $\\ne$ 함숫값</h4>
                    <p class="text-xs text-slate-600">점 하나만 다른 곳에 찍혀 있는 경우 (동떨어진 점)</p>
                </div>
            </div>
            <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
                <h4 class="font-bold text-slate-800 text-sm mb-2">📌 구간의 기호 정리</h4>
                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
                    <div class="p-2 bg-white rounded border border-slate-200">닫힌구간 $[a, b]$ : $a \\le x \\le b$</div>
                    <div class="p-2 bg-white rounded border border-slate-200">열린구간 $(a, b)$ : $a < x < b$</div>
                    <div class="p-2 bg-white rounded border border-slate-200">반열린구간 $[a, b)$ : $a \\le x < b$</div>
                    <div class="p-2 bg-white rounded border border-slate-200">전체 실수 $(-\\infty, \\infty)$</div>
                </div>
            </div>
        </section>

        <!-- Section Interactive Lab -->
        <section id="sec-lab" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center justify-between pb-3 border-b border-slate-200">
                <div class="flex items-center gap-2.5">
                    <span class="w-2.5 h-6 bg-sky-600 rounded-full"></span>
                    <h3 class="text-xl font-bold text-slate-900">함수의 연속성 동적 시뮬레이터</h3>
                </div>
                <span class="text-xs font-bold text-sky-600 bg-sky-50 px-2.5 py-1 rounded-full border border-sky-200">x = 1 에서의 연속 판정</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-center">
                <div class="md:col-span-2 bg-slate-50 rounded-xl p-4 flex flex-col items-center border border-slate-200">
                    <canvas id="cont-canvas" width="500" height="260" class="w-full h-56 rounded-lg bg-white shadow-inner"></canvas>
                </div>
                <div class="space-y-4">
                    <div>
                        <label class="block text-xs font-bold text-slate-600 mb-1">함숫값 $f(1)$ 조절 슬라이더</label>
                        <input type="range" id="f1-slider" min="0.0" max="4.0" step="0.1" value="2.0" class="w-full accent-indigo-600 cursor-pointer">
                        <div class="flex justify-between text-xs text-slate-500 mt-1">
                            <span>0.0</span>
                            <span id="f1-val" class="font-bold text-indigo-600 text-sm">f(1) = 2.0</span>
                            <span>4.0</span>
                        </div>
                    </div>
                    <div class="p-3 bg-slate-50 rounded-xl space-y-2 text-xs border border-slate-200">
                        <div class="flex justify-between">
                            <span class="text-slate-600">함수 $f(x)$ ($x \\ne 1$):</span>
                            <span class="font-bold text-slate-800">$f(x) = x + 1$</span>
                        </div>
                        <div class="flex justify-between">
                            <span class="text-slate-600">극한값 $\\lim_{{x \\to 1}} f(x)$:</span>
                            <span class="font-bold text-indigo-600 text-sm">2.0</span>
                        </div>
                        <div class="flex justify-between border-t border-slate-200 pt-2">
                            <span class="text-slate-600">연속성 판정:</span>
                            <span id="cont-status" class="font-black text-emerald-600 text-sm">연속 (Continuous)</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Section Problems -->
        <section id="sec-ex1" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center gap-2.5 pb-3 border-b border-slate-200">
                <span class="w-2.5 h-6 bg-rose-600 rounded-full"></span>
                <h3 class="text-xl font-bold text-slate-900">대표 예제 풀이 & 연습장</h3>
            </div>
            <div class="p-5 rounded-xl border border-slate-200 bg-slate-50/50 space-y-3">
                <div class="flex items-center justify-between">
                    <span class="px-2.5 py-1 rounded bg-rose-100 text-rose-700 text-xs font-bold">예제 1 (미정계수와 연속)</span>
                    <button onclick="toggleSolution('sol-ex3-1')" class="text-xs font-bold text-indigo-600 hover:underline">풀이 확인</button>
                </div>
                <h4 class="font-bold text-slate-900 text-base">
                    함수 $f(x) = \\begin{{cases}} \\frac{{x^2 - x + a}}{{x - 2}} & (x \\ne 2) \\\\ b & (x = 2) \\end{{cases}}$ 가 $x = 2$에서 연속일 때, 상수 $a, b$의 값을 구하시오.
                </h4>
                <div id="sol-ex3-1" class="hidden p-4 rounded-xl bg-white border border-slate-200 text-sm space-y-2">
                    <p class="text-slate-700">$x=2$에서 연속이려면 $\\lim_{{x \\to 2}} f(x) = f(2) = b$ 이어야 합니다.</p>
                    <p class="text-slate-700">$x \\to 2$일 때 분모 $\\to 0$이므로 분자도 $\\to 0$이어야 합니다: $2^2 - 2 + a = 0 \\implies a = -2$.</p>
                    <p class="font-semibold text-slate-900">$$\\lim_{{x \\to 2}} \\frac{{x^2 - x - 2}}{{x - 2}} = \\lim_{{x \\to 2}} \\frac{{(x-2)(x+1)}}{{x-2}} = \\lim_{{x \\to 2}} (x+1) = 3$$</p>
                    <p class="font-bold text-emerald-600">따라서 $a = -2, b = 3$ 입니다.</p>
                </div>
                <div class="mt-4">
                    <div class="flex justify-between items-center mb-1.5 text-xs text-slate-500">
                        <span><i class="fa-solid fa-pen-nib mr-1"></i> 문제 풀이 연습장</span>
                        <button class="clear-scratchpad-btn hover:text-slate-700 font-bold">지우기</button>
                    </div>
                    <canvas class="scratchpad-canvas w-full h-36 rounded-xl border border-slate-300 bg-white"></canvas>
                </div>
            </div>
        </section>

        <!-- Section Check -->
        <section id="sec-check" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center gap-2.5 pb-3 border-b border-slate-200">
                <span class="w-2.5 h-6 bg-teal-600 rounded-full"></span>
                <h3 class="text-xl font-bold text-slate-900">스스로 확인하기 (형성평가)</h3>
            </div>
            <div class="space-y-4">
                <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
                    <p class="font-bold text-sm mb-2 text-slate-900">01. 함수 $f(x) = \\frac{{1}}{{x-3}}$이 연속인 구간을 기호로 나타내시오.</p>
                    <div class="flex items-center gap-2">
                        <button onclick="toggleSolution('ans-3-01')" class="px-3 py-1 bg-teal-600 hover:bg-teal-700 text-white rounded-lg text-xs font-bold transition">정답 확인</button>
                        <span id="ans-3-01" class="hidden font-bold text-sm text-teal-700">$(-\\infty, 3) \\cup (3, \\infty)$ ($x \\ne 3$인 모든 실수)</span>
                    </div>
                </div>
                <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
                    <p class="font-bold text-sm mb-2 text-slate-900">02. 함수 $f(x) = \\sqrt{{2x - 4}}$가 연속인 구간을 기호로 나타내시오.</p>
                    <div class="flex items-center gap-2">
                        <button onclick="toggleSolution('ans-3-02')" class="px-3 py-1 bg-teal-600 hover:bg-teal-700 text-white rounded-lg text-xs font-bold transition">정답 확인</button>
                        <span id="ans-3-02" class="hidden font-bold text-sm text-teal-700">$[2, \\infty)$ (근호 안 $2x-4 \\ge 0$)</span>
                    </div>
                </div>
                <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
                    <p class="font-bold text-sm mb-2 text-slate-900">03. 다항함수 $f(x) = 2x^2 - 3x + 1$은 모든 실수에서 연속인가?</p>
                    <div class="flex items-center gap-2">
                        <button onclick="toggleSolution('ans-3-03')" class="px-3 py-1 bg-teal-600 hover:bg-teal-700 text-white rounded-lg text-xs font-bold transition">정답 확인</button>
                        <span id="ans-3-03" class="hidden font-bold text-sm text-teal-700">그렇다 (모든 다항함수는 $(-\\infty, \\infty)$에서 연속)</span>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <script>
    const cv3 = document.getElementById('cont-canvas');
    if (cv3) {{
        const ctx = cv3.getContext('2d');
        const s = document.getElementById('f1-slider');
        const f1Val = document.getElementById('f1-val');
        const status = document.getElementById('cont-status');

        function draw3() {{
            const f1 = parseFloat(s.value);
            f1Val.textContent = 'f(1) = ' + f1.toFixed(1);

            const isCont = Math.abs(f1 - 2.0) < 0.05;
            if (isCont) {{
                status.textContent = '연속 (Continuous) : lim = f(1)';
                status.className = 'font-black text-emerald-600 text-sm';
            }} else {{
                status.textContent = '불연속 (Discontinuous) : lim ≠ f(1)';
                status.className = 'font-black text-rose-600 text-sm';
            }}

            ctx.clearRect(0, 0, cv3.width, cv3.height);
            const ox = 120, oy = 210, sx = 80, sy = 40;

            // Grid
            ctx.strokeStyle = '#f1f5f9';
            ctx.lineWidth = 1;
            for(let gx = -1; gx <= 4; gx++) {{
                ctx.beginPath();
                ctx.moveTo(ox + gx * sx, 10);
                ctx.lineTo(ox + gx * sx, oy + 10);
                ctx.stroke();
            }}

            // Axes
            ctx.strokeStyle = '#94a3b8';
            ctx.lineWidth = 1.5;
            ctx.beginPath();
            ctx.moveTo(20, oy); ctx.lineTo(460, oy);
            ctx.moveTo(ox, 10); ctx.lineTo(ox, 230);
            ctx.stroke();

            // Line f(x) = x + 1
            ctx.strokeStyle = '#6366f1';
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.moveTo(ox - 1 * sx, oy - 0 * sy);
            ctx.lineTo(ox + 3.5 * sx, oy - 4.5 * sy);
            ctx.stroke();

            // Hole at (1, 2)
            ctx.fillStyle = '#ffffff';
            ctx.strokeStyle = '#6366f1';
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.arc(ox + 1 * sx, oy - 2 * sy, 6, 0, Math.PI * 2);
            ctx.fill(); ctx.stroke();

            // Movable point at (1, f1)
            ctx.fillStyle = isCont ? '#10b981' : '#ef4444';
            ctx.strokeStyle = '#ffffff';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.arc(ox + 1 * sx, oy - f1 * sy, 6, 0, Math.PI * 2);
            ctx.fill(); ctx.stroke();

            // Labels
            ctx.fillStyle = '#64748b';
            ctx.font = '11px sans-serif';
            ctx.fillText('x=1', ox + 1 * sx - 10, oy + 16);
            ctx.fillText('y=2', ox - 28, oy - 2 * sy + 4);
        }}
        s.addEventListener('input', draw3);
        draw3();
    }}
    </script>
    """

    html = get_header(title, page) + body + get_footer()
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Created:", filename)


def create_unit_4():
    title = "Ⅰ. 함수의 극한과 연속 - 04. 연속함수의 성질"
    page = "35 ~ 41쪽"
    filename = "1. 함수의 극한과 연속 4. 연속함수의 성질.html"

    body = f"""
    <header class="lg:hidden fixed top-0 left-0 right-0 h-16 bg-white/95 backdrop-blur border-b border-slate-200 z-40 flex items-center justify-between px-4">
        <span class="font-bold text-lg text-indigo-600">04. 연속함수의 성질</span>
        <button onclick="toggleWhiteboard()" class="px-2.5 py-1.5 rounded-lg bg-indigo-600 text-white text-xs font-bold flex items-center gap-1">
            <i class="fa-solid fa-chalkboard-user"></i> 칠판
        </button>
    </header>

    <aside id="sidebar" class="fixed top-0 left-0 bottom-0 w-72 bg-white border-r border-slate-200 z-40 flex flex-col justify-between shadow-lg lg:shadow-none">
        <div class="p-5 border-b border-slate-200">
            <span class="text-xs font-extrabold tracking-wider uppercase px-2.5 py-1 rounded-md bg-indigo-100 text-indigo-700">Ⅰ. 함수의 극한과 연속</span>
            <h1 class="text-2xl font-extrabold text-slate-900 mt-2 flex items-center gap-2">
                <i class="fa-solid fa-mountain text-indigo-600"></i>
                <span>04. 연속함수의 성질</span>
            </h1>
            <p class="text-xs text-slate-500 mt-1">교과서 {page}</p>
        </div>
        <nav class="flex-1 overflow-y-auto py-3 px-2 space-y-1">
            <a href="#sec-intro" class="nav-link active flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-lightbulb text-amber-500"></i><span>성취기준 & 생각 열기</span>
            </a>
            <a href="#sec-concept1" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-arrows-up-down text-indigo-500"></i><span>1. 최대·최소 정리</span>
            </a>
            <a href="#sec-concept2" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-crosshairs text-emerald-500"></i><span>2. 사잇값 정리 & 실근 존재</span>
            </a>
            <a href="#sec-lab" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-sliders text-sky-500"></i><span>사잇값 정리 인터랙티브 실험</span>
            </a>
            <a href="#sec-ex1" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-pen-to-square text-rose-500"></i><span>대표 예제 & 연습장</span>
            </a>
            <a href="#sec-check" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-clipboard-check text-teal-500"></i><span>스스로 확인하기 (01~04)</span>
            </a>
        </nav>
        <div class="p-3 border-t border-slate-200 bg-slate-50 no-print">
            <button onclick="toggleWhiteboard()" class="w-full py-2 px-3 rounded-xl bg-gradient-to-r from-indigo-600 to-sky-600 hover:from-indigo-500 hover:to-sky-500 text-white text-xs font-extrabold shadow-sm flex items-center justify-center gap-2 transition cursor-pointer">
                <i class="fa-solid fa-chalkboard-user"></i>
                <span>전자칠판 판서 모드</span>
            </button>
        </div>
    </aside>

    <main id="main-content" class="lg:ml-72 min-h-screen p-6 sm:p-10 space-y-12">
        <section id="sec-intro" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-50 text-indigo-700 text-xs font-bold mb-4">
                <i class="fa-solid fa-compass"></i> 성취기준
            </div>
            <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 mb-4">
                연속함수의 성질을 이해하고, 최대·최소 정리와 사잇값 정리를 활용할 수 있다
            </h2>
            <div class="bg-indigo-50/70 rounded-xl p-5 border border-indigo-100">
                <h3 class="font-bold text-indigo-900 text-base mb-2">💡 생각 열기 : 흔들리지 않고 강을 건너는 다리?</h3>
                <p class="text-sm text-slate-700 leading-relaxed">
                    어떤 물체가 영하 $5^\\circ\\text{{C}}$에서 영상 $15^\\circ\\text{{C}}$로 온도가 변했습니다. 온도는 연속적으로 변하므로 도중에 반드시 $0^\\circ\\text{{C}}$가 되는 순간이 존재할까요?
                </p>
                <div class="mt-3 flex items-center gap-3">
                    <button onclick="toggleSolution('intro-ans4')" class="text-xs font-bold text-indigo-600 hover:underline">정답 확인</button>
                    <span id="intro-ans4" class="hidden text-xs font-bold text-emerald-600">네! 온도는 연속함수이므로 사잇값 정리에 의해 $-5$와 $15$ 사이의 $0$을 반드시 거쳐 지나갑니다.</span>
                </div>
            </div>
        </section>

        <section id="sec-concept1" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center gap-2.5 pb-3 border-b border-slate-200">
                <span class="w-2.5 h-6 bg-indigo-600 rounded-full"></span>
                <h3 class="text-xl font-bold text-slate-900">1. 최대·최소 정리 (Extreme Value Theorem)</h3>
            </div>
            <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                <div class="p-4 bg-white rounded-xl border border-indigo-200 shadow-xs">
                    <h4 class="font-bold text-indigo-900 text-base mb-2">📌 정리 내용</h4>
                    <p class="text-sm text-slate-800 leading-relaxed">
                        함수 $f(x)$가 <b>닫힌구간 $[a, b]$에서 연속</b>이면, $f(x)$는 이 구간에서 반드시 <b>최댓값</b>과 <b>최솟값</b>을 갖는다.
                    </p>
                </div>
                <div class="p-3 rounded-lg bg-amber-50 border border-amber-200 text-xs text-amber-900">
                    <i class="fa-solid fa-triangle-exclamation mr-1 text-amber-600"></i>
                    <b>전제 조건 필수:</b> 닫힌구간이 아니거나(열린구간), 연속이 아니면 최댓값 또는 최솟값이 존재하지 않을 수 있습니다.
                </div>
            </div>
        </section>

        <section id="sec-concept2" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center gap-2.5 pb-3 border-b border-slate-200">
                <span class="w-2.5 h-6 bg-emerald-600 rounded-full"></span>
                <h3 class="text-xl font-bold text-slate-900">2. 사잇값 정리 & 방정식의 실근의 존재</h3>
            </div>
            <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-4">
                <div class="p-4 bg-white rounded-xl border border-emerald-200 shadow-xs">
                    <h4 class="font-bold text-emerald-900 text-base mb-2">📌 사잇값 정리</h4>
                    <p class="text-sm text-slate-800 leading-relaxed">
                        함수 $f(x)$가 닫힌구간 $[a, b]$에서 연속이고 $f(a) \\ne f(b)$일 때, $f(a)$와 $f(b)$ 사이의 임의의 값 $k$에 대하여
                        $$f(c) = k$$
                        인 $c$가 열린구간 $(a, b)$에 적어도 하나 존재한다.
                    </p>
                </div>
                <div class="p-4 bg-white rounded-xl border border-sky-200 shadow-xs">
                    <h4 class="font-bold text-sky-900 text-base mb-2">🎯 실근의 존재 판정 (k = 0 인 경우)</h4>
                    <p class="text-sm text-slate-800 leading-relaxed">
                        함수 $f(x)$가 닫힌구간 $[a, b]$에서 연속이고 <b>$f(a)f(b) < 0$</b> (부호가 반대)이면,
                        방정식 $f(x) = 0$은 열린구간 $(a, b)$에서 <b>적어도 하나의 실근</b>을 갖는다.
                    </p>
                </div>
            </div>
        </section>

        <!-- Section Interactive Lab -->
        <section id="sec-lab" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center justify-between pb-3 border-b border-slate-200">
                <div class="flex items-center gap-2.5">
                    <span class="w-2.5 h-6 bg-sky-600 rounded-full"></span>
                    <h3 class="text-xl font-bold text-slate-900">사잇값 정리 실근 탐색 실험실</h3>
                </div>
                <span class="text-xs font-bold text-sky-600 bg-sky-50 px-2.5 py-1 rounded-full border border-sky-200">f(x) = x³ - 3x - 1</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-center">
                <div class="md:col-span-2 bg-slate-50 rounded-xl p-4 flex flex-col items-center border border-slate-200">
                    <canvas id="ivt-canvas" width="500" height="260" class="w-full h-56 rounded-lg bg-white shadow-inner"></canvas>
                </div>
                <div class="space-y-4">
                    <div>
                        <label class="block text-xs font-bold text-slate-600 mb-1">구간 끝점 b 조절 슬라이더 (a = 1.0 고정)</label>
                        <input type="range" id="b-slider" min="1.2" max="2.5" step="0.05" value="2.0" class="w-full accent-sky-600 cursor-pointer">
                        <div class="flex justify-between text-xs text-slate-500 mt-1">
                            <span>b = 1.2</span>
                            <span id="b-val" class="font-bold text-sky-600 text-sm">b = 2.00</span>
                            <span>b = 2.5</span>
                        </div>
                    </div>
                    <div class="p-3 bg-slate-50 rounded-xl space-y-2 text-xs border border-slate-200">
                        <div class="flex justify-between">
                            <span class="text-slate-600">f(a) = f(1.0):</span>
                            <span class="font-bold text-rose-600">-3.00 (음수)</span>
                        </div>
                        <div class="flex justify-between">
                            <span class="text-slate-600">f(b):</span>
                            <span id="fb-val" class="font-bold text-emerald-600">1.00 (양수)</span>
                        </div>
                        <div class="flex justify-between border-t border-slate-200 pt-2">
                            <span class="text-slate-600">실근 존재 여부:</span>
                            <span id="root-status" class="font-black text-emerald-600 text-sm">실근 존재 (f(a)·f(b) < 0)</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Section Problems -->
        <section id="sec-ex1" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center gap-2.5 pb-3 border-b border-slate-200">
                <span class="w-2.5 h-6 bg-rose-600 rounded-full"></span>
                <h3 class="text-xl font-bold text-slate-900">대표 예제 풀이 & 연습장</h3>
            </div>
            <div class="p-5 rounded-xl border border-slate-200 bg-slate-50/50 space-y-3">
                <div class="flex items-center justify-between">
                    <span class="px-2.5 py-1 rounded bg-rose-100 text-rose-700 text-xs font-bold">예제 1 (사잇값 정리와 실근 증명)</span>
                    <button onclick="toggleSolution('sol-ex4-1')" class="text-xs font-bold text-indigo-600 hover:underline">풀이 확인</button>
                </div>
                <h4 class="font-bold text-slate-900 text-base">
                    방정식 $x^3 - 3x - 1 = 0$ 이 열린구간 $(1, 2)$에서 적어도 하나의 실근을 가짐을 보이시오.
                </h4>
                <div id="sol-ex4-1" class="hidden p-4 rounded-xl bg-white border border-slate-200 text-sm space-y-2">
                    <p class="text-slate-700">$f(x) = x^3 - 3x - 1$이라 두면 $f(x)$는 다항함수이므로 닫힌구간 $[1, 2]$에서 연속입니다.</p>
                    <p class="font-semibold text-slate-900">$$f(1) = 1 - 3 - 1 = -3 < 0$$</p>
                    <p class="font-semibold text-slate-900">$$f(2) = 8 - 6 - 1 = 1 > 0$$</p>
                    <p class="text-slate-700">$f(1)$과 $f(2)$의 부호가 서로 다르므로($f(1)f(2) < 0$), 사잇값 정리에 의해 $f(c) = 0$인 $c$가 열린구간 $(1, 2)$에 적어도 하나 존재합니다.</p>
                </div>
                <div class="mt-4">
                    <div class="flex justify-between items-center mb-1.5 text-xs text-slate-500">
                        <span><i class="fa-solid fa-pen-nib mr-1"></i> 문제 풀이 연습장</span>
                        <button class="clear-scratchpad-btn hover:text-slate-700 font-bold">지우기</button>
                    </div>
                    <canvas class="scratchpad-canvas w-full h-36 rounded-xl border border-slate-300 bg-white"></canvas>
                </div>
            </div>
        </section>

        <!-- Section Check -->
        <section id="sec-check" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center gap-2.5 pb-3 border-b border-slate-200">
                <span class="w-2.5 h-6 bg-teal-600 rounded-full"></span>
                <h3 class="text-xl font-bold text-slate-900">스스로 확인하기 (형성평가)</h3>
            </div>
            <div class="space-y-4">
                <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
                    <p class="font-bold text-sm mb-2 text-slate-900">01. 함수 $f(x) = -x^2 + 2x + 3$의 닫힌구간 $[0, 3]$에서의 최댓값과 최솟값은?</p>
                    <div class="flex items-center gap-2">
                        <button onclick="toggleSolution('ans-4-01')" class="px-3 py-1 bg-teal-600 hover:bg-teal-700 text-white rounded-lg text-xs font-bold transition">정답 확인</button>
                        <span id="ans-4-01" class="hidden font-bold text-sm text-teal-700">최댓값 $4$ ($x=1$), 최솟값 $0$ ($x=3$)</span>
                    </div>
                </div>
                <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
                    <p class="font-bold text-sm mb-2 text-slate-900">02. 방정식 $x^3 + 2x - 5 = 0$은 구간 $(1, 2)$에서 실근을 갖는가?</p>
                    <div class="flex items-center gap-2">
                        <button onclick="toggleSolution('ans-4-02')" class="px-3 py-1 bg-teal-600 hover:bg-teal-700 text-white rounded-lg text-xs font-bold transition">정답 확인</button>
                        <span id="ans-4-02" class="hidden font-bold text-sm text-teal-700">갖는다 ($f(1) = -2 < 0$, $f(2) = 7 > 0$)</span>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <script>
    const cv4 = document.getElementById('ivt-canvas');
    if (cv4) {{
        const ctx = cv4.getContext('2d');
        const bSlider = document.getElementById('b-slider');
        const bVal = document.getElementById('b-val');
        const fbVal = document.getElementById('fb-val');
        const rootStatus = document.getElementById('root-status');

        function f(x) {{ return x*x*x - 3*x - 1; }}

        function draw4() {{
            const b = parseFloat(bSlider.value);
            const fb = f(b);
            bVal.textContent = 'b = ' + b.toFixed(2);
            fbVal.textContent = fb.toFixed(2) + (fb > 0 ? ' (양수)' : ' (음수)');

            const hasRoot = fb > 0;
            if (hasRoot) {{
                rootStatus.textContent = '실근 존재! f(a)·f(b) < 0';
                rootStatus.className = 'font-black text-emerald-600 text-sm';
            }} else {{
                rootStatus.textContent = '부호 동일 (실근 보장 못함)';
                rootStatus.className = 'font-black text-amber-600 text-sm';
            }}

            ctx.clearRect(0, 0, cv4.width, cv4.height);
            const ox = 150, oy = 130, sx = 90, sy = 25;

            // Coordinate Grid & Axes
            ctx.strokeStyle = '#94a3b8';
            ctx.lineWidth = 1.5;
            ctx.beginPath();
            ctx.moveTo(20, oy); ctx.lineTo(460, oy);
            ctx.moveTo(ox, 10); ctx.lineTo(ox, 240);
            ctx.stroke();

            // Labels
            ctx.fillStyle = '#64748b';
            ctx.font = '11px sans-serif';
            ctx.fillText('x', 450, oy - 6);
            ctx.fillText('y', ox + 6, 20);
            ctx.fillText('O', ox - 14, oy + 14);

            // Curve f(x)
            ctx.strokeStyle = '#0284c7';
            ctx.lineWidth = 2.5;
            ctx.beginPath();
            for(let px = 0.5; px <= 2.6; px += 0.05) {{
                const py = f(px);
                const cx = ox + px * sx;
                const cy = oy - py * sy;
                if (px === 0.5) ctx.moveTo(cx, cy);
                else ctx.lineTo(cx, cy);
            }}
            ctx.stroke();

            // Point A (1, -3)
            const fa = f(1.0);
            ctx.fillStyle = '#ef4444';
            ctx.beginPath();
            ctx.arc(ox + 1.0 * sx, oy - fa * sy, 6, 0, Math.PI * 2);
            ctx.fill();

            // Point B (b, fb)
            ctx.fillStyle = fb > 0 ? '#10b981' : '#f59e0b';
            ctx.beginPath();
            ctx.arc(ox + b * sx, oy - fb * sy, 6, 0, Math.PI * 2);
            ctx.fill();

            // Root mark (approx 1.88)
            if (b >= 1.88) {{
                ctx.fillStyle = '#8b5cf6';
                ctx.beginPath();
                ctx.arc(ox + 1.88 * sx, oy, 5, 0, Math.PI * 2);
                ctx.fill();
                ctx.fillText('실근 c ≈ 1.88', ox + 1.88 * sx - 25, oy - 10);
            }}
        }}
        bSlider.addEventListener('input', draw4);
        draw4();
    }}
    </script>
    """

    html = get_header(title, page) + body + get_footer()
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Created:", filename)


def create_unit_5():
    title = "Ⅰ. 함수의 극한과 연속 - 대단원 마무리"
    page = "42 ~ 47쪽"
    filename = "1. 함수의 극한과 연속 대단원마무리.html"

    body = f"""
    <header class="lg:hidden fixed top-0 left-0 right-0 h-16 bg-white/95 backdrop-blur border-b border-slate-200 z-40 flex items-center justify-between px-4">
        <span class="font-bold text-lg text-indigo-600">Ⅰ. 대단원 마무리</span>
        <button onclick="toggleWhiteboard()" class="px-2.5 py-1.5 rounded-lg bg-indigo-600 text-white text-xs font-bold flex items-center gap-1">
            <i class="fa-solid fa-chalkboard-user"></i> 칠판
        </button>
    </header>

    <aside id="sidebar" class="fixed top-0 left-0 bottom-0 w-72 bg-white border-r border-slate-200 z-40 flex flex-col justify-between shadow-lg lg:shadow-none">
        <div class="p-5 border-b border-slate-200">
            <span class="text-xs font-extrabold tracking-wider uppercase px-2.5 py-1 rounded-md bg-indigo-100 text-indigo-700">Ⅰ. 함수의 극한과 연속</span>
            <h1 class="text-2xl font-extrabold text-slate-900 mt-2 flex items-center gap-2">
                <i class="fa-solid fa-award text-indigo-600"></i>
                <span>대단원 마무리</span>
            </h1>
            <p class="text-xs text-slate-500 mt-1">교과서 {page}</p>
        </div>
        <nav class="flex-1 overflow-y-auto py-3 px-2 space-y-1">
            <a href="#sec-summary" class="nav-link active flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-sitemap text-amber-500"></i><span>1단원 핵심 개념 총정리</span>
            </a>
            <a href="#sec-prob-basic" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-seedling text-emerald-500"></i><span>기본 문제 (01~02)</span>
            </a>
            <a href="#sec-prob-standard" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-tree text-indigo-500"></i><span>표준 문제 (03~04)</span>
            </a>
            <a href="#sec-prob-advanced" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-fire text-rose-500"></i><span>발전 & 서술형 (05~06)</span>
            </a>
        </nav>
        <div class="p-3 border-t border-slate-200 bg-slate-50 no-print">
            <button onclick="toggleWhiteboard()" class="w-full py-2 px-3 rounded-xl bg-gradient-to-r from-indigo-600 to-sky-600 hover:from-indigo-500 hover:to-sky-500 text-white text-xs font-extrabold shadow-sm flex items-center justify-center gap-2 transition cursor-pointer">
                <i class="fa-solid fa-chalkboard-user"></i>
                <span>전자칠판 판서 모드</span>
            </button>
        </div>
    </aside>

    <main id="main-content" class="lg:ml-72 min-h-screen p-6 sm:p-10 space-y-12">
        <section id="sec-summary" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center gap-2.5 pb-3 border-b border-slate-200">
                <span class="w-2.5 h-6 bg-indigo-600 rounded-full"></span>
                <h2 class="text-2xl font-extrabold text-slate-900">Ⅰ. 함수의 극한과 연속 핵심 개념 마인드맵</h2>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <h3 class="font-bold text-indigo-900 text-base flex items-center gap-2">
                        <i class="fa-solid fa-calculator text-indigo-600"></i> 1. 함수의 극한
                    </h3>
                    <ul class="text-xs text-slate-700 space-y-1.5 list-disc list-inside">
                        <li><b>수렴과 발산:</b> $\\lim_{{x \\to a}} f(x) = L$ (우극한 = 좌극한)</li>
                        <li><b>기본 성질:</b> 수렴할 때 사칙연산 분배 가능</li>
                        <li><b>부정형:</b> $\\frac{{0}}{{0}}$ (인수분해/유리화), $\\frac{{\\infty}}{{\\infty}}$ (최고차항 나누기)</li>
                        <li><b>조임정리:</b> $g(x) \\le f(x) \\le h(x)$이고 양끝 극한이 같으면 가운데도 동일</li>
                    </ul>
                </div>
                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <h3 class="font-bold text-emerald-900 text-base flex items-center gap-2">
                        <i class="fa-solid fa-link text-emerald-600"></i> 2. 함수의 연속
                    </h3>
                    <ul class="text-xs text-slate-700 space-y-1.5 list-disc list-inside">
                        <li><b>연속 조건:</b> ① $f(a)$ 정의, ② $\\lim_{{x \\to a}} f(x)$ 존재, ③ 두 값 일치</li>
                        <li><b>최대·최소 정리:</b> 닫힌구간에서 연속이면 반드시 최댓값, 최솟값 존재</li>
                        <li><b>사잇값 정리:</b> 닫힌구간 연속 & $f(a) \\ne f(b)$이면 사잇값 $k$를 만족하는 $c$ 존재</li>
                        <li><b>실근 판정:</b> $f(a)f(b) < 0$이면 열린구간 $(a, b)$에서 적어도 하나의 실근 가짐</li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- Basic Problems -->
        <section id="sec-prob-basic" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center gap-2.5 pb-3 border-b border-slate-200">
                <span class="w-2.5 h-6 bg-emerald-600 rounded-full"></span>
                <h3 class="text-xl font-bold text-slate-900">기본 평가 문제 (01 ~ 02)</h3>
            </div>
            
            <div class="p-5 rounded-xl border border-slate-200 bg-slate-50/50 space-y-3">
                <div class="flex items-center justify-between">
                    <span class="px-2.5 py-1 rounded bg-emerald-100 text-emerald-800 text-xs font-bold">문제 01 (극한 계산)</span>
                    <button onclick="toggleSolution('sol-d1-1')" class="text-xs font-bold text-indigo-600 hover:underline">풀이 확인</button>
                </div>
                <p class="font-bold text-slate-900 text-base">다음 극한값을 구하시오: $\\lim_{{x \\to 2}} \\frac{{x^2 + x - 6}}{{x - 2}}$</p>
                <div id="sol-d1-1" class="hidden p-4 rounded-xl bg-white border border-slate-200 text-sm space-y-2">
                    <p class="text-slate-700">분자를 인수분해하면 $(x-2)(x+3)$입니다.</p>
                    <p class="font-semibold text-slate-900">$$\\lim_{{x \\to 2}} \\frac{{(x-2)(x+3)}}{{x-2}} = \\lim_{{x \\to 2}} (x+3) = 5$$</p>
                </div>
                <div class="mt-4">
                    <div class="flex justify-between items-center mb-1.5 text-xs text-slate-500">
                        <span><i class="fa-solid fa-pen-nib mr-1"></i> 문제 풀이 연습장</span>
                        <button class="clear-scratchpad-btn hover:text-slate-700 font-bold">지우기</button>
                    </div>
                    <canvas class="scratchpad-canvas w-full h-32 rounded-xl border border-slate-300 bg-white"></canvas>
                </div>
            </div>

            <div class="p-5 rounded-xl border border-slate-200 bg-slate-50/50 space-y-3">
                <div class="flex items-center justify-between">
                    <span class="px-2.5 py-1 rounded bg-emerald-100 text-emerald-800 text-xs font-bold">문제 02 (무한대 극한)</span>
                    <button onclick="toggleSolution('sol-d1-2')" class="text-xs font-bold text-indigo-600 hover:underline">풀이 확인</button>
                </div>
                <p class="font-bold text-slate-900 text-base">다음 극한값을 구하시오: $\\lim_{{x \\to \\infty}} (\\sqrt{{x^2 + 4x}} - x)$</p>
                <div id="sol-d1-2" class="hidden p-4 rounded-xl bg-white border border-slate-200 text-sm space-y-2">
                    <p class="text-slate-700">분자를 유리화합니다:</p>
                    <p class="font-semibold text-slate-900">$$\\lim_{{x \\to \\infty}} \\frac{{(x^2 + 4x) - x^2}}{{\\sqrt{{x^2 + 4x}} + x}} = \\lim_{{x \\to \\infty}} \\frac{{4x}}{{\\sqrt{{x^2 + 4x}} + x}} = \\frac{{4}}{{1 + 1}} = 2$$</p>
                </div>
                <div class="mt-4">
                    <div class="flex justify-between items-center mb-1.5 text-xs text-slate-500">
                        <span><i class="fa-solid fa-pen-nib mr-1"></i> 문제 풀이 연습장</span>
                        <button class="clear-scratchpad-btn hover:text-slate-700 font-bold">지우기</button>
                    </div>
                    <canvas class="scratchpad-canvas w-full h-32 rounded-xl border border-slate-300 bg-white"></canvas>
                </div>
            </div>
        </section>

        <!-- Standard Problems -->
        <section id="sec-prob-standard" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center gap-2.5 pb-3 border-b border-slate-200">
                <span class="w-2.5 h-6 bg-indigo-600 rounded-full"></span>
                <h3 class="text-xl font-bold text-slate-900">표준 평가 문제 (03 ~ 04)</h3>
            </div>
            
            <div class="p-5 rounded-xl border border-slate-200 bg-slate-50/50 space-y-3">
                <div class="flex items-center justify-between">
                    <span class="px-2.5 py-1 rounded bg-indigo-100 text-indigo-800 text-xs font-bold">문제 03 (미정계수 결정)</span>
                    <button onclick="toggleSolution('sol-d1-3')" class="text-xs font-bold text-indigo-600 hover:underline">풀이 확인</button>
                </div>
                <p class="font-bold text-slate-900 text-base">$\\lim_{{x \\to 1}} \\frac{{x^2 + ax + b}}{{x - 1}} = 3$ 을 만족시키는 상수 $a, b$에 대하여 $a - b$의 값을 구하시오.</p>
                <div id="sol-d1-3" class="hidden p-4 rounded-xl bg-white border border-slate-200 text-sm space-y-2">
                    <p class="text-slate-700">분모 $\\to 0$이므로 분자 $1 + a + b = 0 \\implies b = -a - 1$.</p>
                    <p class="text-slate-700">분자 $x^2 + ax - a - 1 = (x-1)(x + a + 1)$.</p>
                    <p class="font-semibold text-slate-900">$$\\lim_{{x \\to 1}} (x + a + 1) = a + 2 = 3 \\implies a = 1, b = -2$$</p>
                    <p class="font-bold text-emerald-600">따라서 $a - b = 1 - (-2) = 3$ 입니다.</p>
                </div>
                <div class="mt-4">
                    <div class="flex justify-between items-center mb-1.5 text-xs text-slate-500">
                        <span><i class="fa-solid fa-pen-nib mr-1"></i> 문제 풀이 연습장</span>
                        <button class="clear-scratchpad-btn hover:text-slate-700 font-bold">지우기</button>
                    </div>
                    <canvas class="scratchpad-canvas w-full h-32 rounded-xl border border-slate-300 bg-white"></canvas>
                </div>
            </div>

            <div class="p-5 rounded-xl border border-slate-200 bg-slate-50/50 space-y-3">
                <div class="flex items-center justify-between">
                    <span class="px-2.5 py-1 rounded bg-indigo-100 text-indigo-800 text-xs font-bold">문제 04 (연속성과 미정계수)</span>
                    <button onclick="toggleSolution('sol-d1-4')" class="text-xs font-bold text-indigo-600 hover:underline">풀이 확인</button>
                </div>
                <p class="font-bold text-slate-900 text-base">모든 실수에서 연속인 함수 $f(x)$가 $(x-2)f(x) = x^2 + ax - 6$ 을 만족시킬 때, $f(2)$의 값을 구하시오.</p>
                <div id="sol-d1-4" class="hidden p-4 rounded-xl bg-white border border-slate-200 text-sm space-y-2">
                    <p class="text-slate-700">$x=2$를 대입하면 $0 = 4 + 2a - 6 \\implies 2a = 2 \\implies a = 1$.</p>
                    <p class="text-slate-700">$f(x)$가 연속이므로 $f(2) = \\lim_{{x \\to 2}} f(x) = \\lim_{{x \\to 2}} \\frac{{x^2 + x - 6}}{{x - 2}} = \\lim_{{x \\to 2}} (x+3) = 5$.</p>
                </div>
                <div class="mt-4">
                    <div class="flex justify-between items-center mb-1.5 text-xs text-slate-500">
                        <span><i class="fa-solid fa-pen-nib mr-1"></i> 문제 풀이 연습장</span>
                        <button class="clear-scratchpad-btn hover:text-slate-700 font-bold">지우기</button>
                    </div>
                    <canvas class="scratchpad-canvas w-full h-32 rounded-xl border border-slate-300 bg-white"></canvas>
                </div>
            </div>
        </section>

        <!-- Advanced Problems -->
        <section id="sec-prob-advanced" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center gap-2.5 pb-3 border-b border-slate-200">
                <span class="w-2.5 h-6 bg-rose-600 rounded-full"></span>
                <h3 class="text-xl font-bold text-slate-900">발전 & 수능형 서술형 문제 (05 ~ 06)</h3>
            </div>
            
            <div class="p-5 rounded-xl border border-slate-200 bg-slate-50/50 space-y-3">
                <div class="flex items-center justify-between">
                    <span class="px-2.5 py-1 rounded bg-rose-100 text-rose-800 text-xs font-bold">문제 05 (사잇값 정리의 활용)</span>
                    <button onclick="toggleSolution('sol-d1-5')" class="text-xs font-bold text-indigo-600 hover:underline">풀이 확인</button>
                </div>
                <p class="font-bold text-slate-900 text-base">연속함수 $f(x)$에 대하여 $f(0) = 1, f(1) = -2, f(2) = 3, f(3) = 1$ 일 때, 방정식 $f(x) = 0$은 열린구간 $(0, 3)$에서 적어도 몇 개의 실근을 갖는가?</p>
                <div id="sol-d1-5" class="hidden p-4 rounded-xl bg-white border border-slate-200 text-sm space-y-2">
                    <p class="text-slate-700">• 구간 $(0, 1)$: $f(0)f(1) = 1 \\times (-2) = -2 < 0 \\implies$ 적어도 1개 실근</p>
                    <p class="text-slate-700">• 구간 $(1, 2)$: $f(1)f(2) = (-2) \\times 3 = -6 < 0 \\implies$ 적어도 1개 실근</p>
                    <p class="text-slate-700">• 구간 $(2, 3)$: $f(2)f(3) = 3 \\times 1 = 3 > 0$</p>
                    <p class="font-bold text-emerald-600">따라서 열린구간 $(0, 3)$에서 적어도 2개의 실근을 갖습니다.</p>
                </div>
                <div class="mt-4">
                    <div class="flex justify-between items-center mb-1.5 text-xs text-slate-500">
                        <span><i class="fa-solid fa-pen-nib mr-1"></i> 문제 풀이 연습장</span>
                        <button class="clear-scratchpad-btn hover:text-slate-700 font-bold">지우기</button>
                    </div>
                    <canvas class="scratchpad-canvas w-full h-32 rounded-xl border border-slate-300 bg-white"></canvas>
                </div>
            </div>

            <div class="p-5 rounded-xl border border-slate-200 bg-slate-50/50 space-y-3">
                <div class="flex items-center justify-between">
                    <span class="px-2.5 py-1 rounded bg-rose-100 text-rose-800 text-xs font-bold">문제 06 (다항함수 추론 수능형)</span>
                    <button onclick="toggleSolution('sol-d1-6')" class="text-xs font-bold text-indigo-600 hover:underline">풀이 확인</button>
                </div>
                <p class="font-bold text-slate-900 text-base">다항함수 $f(x)$가 $\\lim_{{x \\to \\infty}} \\frac{{f(x)}}{{2x^2 + 1}} = 1$, $\\lim_{{x \\to 0}} \\frac{{f(x)}}{{x}} = 3$ 을 만족할 때, $f(2)$의 값을 구하시오.</p>
                <div id="sol-d1-6" class="hidden p-4 rounded-xl bg-white border border-slate-200 text-sm space-y-2">
                    <p class="text-slate-700">1) 첫 번째 조건: $f(x)$는 최고차항이 $2x^2$인 2차 다항함수입니다.</p>
                    <p class="text-slate-700">2) 두 번째 조건: $x \\to 0$일 때 분모 $\\to 0$이므로 $f(0) = 0$ (상수항 0).</p>
                    <p class="text-slate-700">따라서 $f(x) = 2x^2 + ax$로 둘 수 있고, $\\lim_{{x \\to 0}} \\frac{{2x^2 + ax}}{{x}} = a = 3$.</p>
                    <p class="font-semibold text-slate-900">$$f(x) = 2x^2 + 3x \\implies f(2) = 2(4) + 3(2) = 8 + 6 = 14$$</p>
                </div>
                <div class="mt-4">
                    <div class="flex justify-between items-center mb-1.5 text-xs text-slate-500">
                        <span><i class="fa-solid fa-pen-nib mr-1"></i> 문제 풀이 연습장</span>
                        <button class="clear-scratchpad-btn hover:text-slate-700 font-bold">지우기</button>
                    </div>
                    <canvas class="scratchpad-canvas w-full h-32 rounded-xl border border-slate-300 bg-white"></canvas>
                </div>
            </div>
        </section>
    </main>
    """

    html = get_header(title, page) + body + get_footer()
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Created:", filename)


if __name__ == '__main__':
    create_unit_3()
    create_unit_4()
    create_unit_5()
