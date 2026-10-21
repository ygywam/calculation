import os
from generate_common import get_header, get_footer

def create_unit_9():
    title = "Ⅱ. 미분 - 04. 접선의 방정식"
    page = "69 ~ 72쪽"
    filename = "2. 미분 4. 접선의 방정식.html"

    body = f"""
    <header class="lg:hidden fixed top-0 left-0 right-0 h-16 bg-white/95 backdrop-blur border-b border-slate-200 z-40 flex items-center justify-between px-4">
        <span class="font-bold text-lg text-indigo-600">04. 접선의 방정식</span>
        <button onclick="toggleWhiteboard()" class="px-2.5 py-1.5 rounded-lg bg-indigo-600 text-white text-xs font-bold flex items-center gap-1">
            <i class="fa-solid fa-chalkboard-user"></i> 칠판
        </button>
    </header>

    <aside id="sidebar" class="fixed top-0 left-0 bottom-0 w-72 bg-white border-r border-slate-200 z-40 flex flex-col justify-between shadow-lg lg:shadow-none">
        <div class="p-5 border-b border-slate-200">
            <span class="text-xs font-extrabold tracking-wider uppercase px-2.5 py-1 rounded-md bg-indigo-100 text-indigo-700">Ⅱ. 미분</span>
            <h1 class="text-2xl font-extrabold text-slate-900 mt-2 flex items-center gap-2">
                <i class="fa-solid fa-lines-leaning text-indigo-600"></i>
                <span>04. 접선의 방정식</span>
            </h1>
            <p class="text-xs text-slate-500 mt-1">교과서 {page}</p>
        </div>
        <nav class="flex-1 overflow-y-auto py-3 px-2 space-y-1">
            <a href="#sec-intro" class="nav-link active flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-lightbulb text-amber-500"></i><span>성취기준 & 생각 열기</span>
            </a>
            <a href="#sec-concept1" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-ruler-combined text-indigo-500"></i><span>1. 접선의 방정식 구하는 3가지 유형</span>
            </a>
            <a href="#sec-lab" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-sliders text-sky-500"></i><span>동적 접선 시뮬레이터</span>
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
                접선의 방정식을 구할 수 있다
            </h2>
            <div class="bg-indigo-50/70 rounded-xl p-5 border border-indigo-100">
                <h3 class="font-bold text-indigo-900 text-base mb-2">💡 생각 열기 : 롤러코스터 트랙을 벗어나는 순간의 궤적은?</h3>
                <p class="text-sm text-slate-700 leading-relaxed">
                    곡선 궤도를 달리던 물체가 트랙에서 이탈하면 접선 방향으로 직진합니다. 곡선 $y = f(x)$ 위의 한 점을 지나며 그 순간의 진행 방향과 일치하는 직선의 방정식을 어떻게 구할 수 있을까요?
                </p>
                <div class="mt-3 flex items-center gap-3">
                    <button onclick="toggleSolution('intro-ans9')" class="text-xs font-bold text-indigo-600 hover:underline">정답 확인</button>
                    <span id="intro-ans9" class="hidden text-xs font-bold text-emerald-600">지나는 점 $(x_1, y_1)$과 미분계수 기울기 $m = f'(x_1)$을 이용해 직선의 방정식을 세웁니다!</span>
                </div>
            </div>
        </section>

        <section id="sec-concept1" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center gap-2.5 pb-3 border-b border-slate-200">
                <span class="w-2.5 h-6 bg-indigo-600 rounded-full"></span>
                <h3 class="text-xl font-bold text-slate-900">1. 접선의 방정식을 구하는 3가지 유형</h3>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-2">
                    <span class="text-xs font-bold px-2 py-0.5 rounded bg-indigo-100 text-indigo-700">유형 1</span>
                    <h4 class="font-bold text-slate-900 text-sm">곡선 위의 점 $(x_1, y_1)$</h4>
                    <p class="text-xs text-slate-600">기울기 $m = f'(x_1)$을 구한 후 공식 적용:</p>
                    <div class="p-2 bg-white rounded border border-slate-200 text-xs font-bold text-indigo-600">
                        $$y - y_1 = f'(x_1)(x - x_1)$$
                    </div>
                </div>

                <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-2">
                    <span class="text-xs font-bold px-2 py-0.5 rounded bg-emerald-100 text-emerald-700">유형 2</span>
                    <h4 class="font-bold text-slate-900 text-sm">기울기 $m$이 주어진 경우</h4>
                    <p class="text-xs text-slate-600">도함수 방정식 $f'(t) = m$을 풀어 접점 $(t, f(t))$를 구한 후 유형 1 공식 적용.</p>
                </div>

                <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-2">
                    <span class="text-xs font-bold px-2 py-0.5 rounded bg-rose-100 text-rose-700">유형 3</span>
                    <h4 class="font-bold text-slate-900 text-sm">곡선 밖의 점 $(x_0, y_0)$</h4>
                    <p class="text-xs text-slate-600">접점을 $(t, f(t))$로 놓고 접선 식을 세운 뒤, 점 $(x_0, y_0)$를 대입하여 $t$를 구함.</p>
                </div>
            </div>
        </section>

        <!-- Section Interactive Lab -->
        <section id="sec-lab" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center justify-between pb-3 border-b border-slate-200">
                <div class="flex items-center gap-2.5">
                    <span class="w-2.5 h-6 bg-sky-600 rounded-full"></span>
                    <h3 class="text-xl font-bold text-slate-900">동적 접선 시뮬레이터</h3>
                </div>
                <span class="text-xs font-bold text-sky-600 bg-sky-50 px-2.5 py-1 rounded-full border border-sky-200">f(x) = x³ - 3x</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-center">
                <div class="md:col-span-2 bg-slate-50 rounded-xl p-4 flex flex-col items-center border border-slate-200">
                    <canvas id="tan-canvas" width="500" height="260" class="w-full h-56 rounded-lg bg-white shadow-inner"></canvas>
                </div>
                <div class="space-y-4">
                    <div>
                        <label class="block text-xs font-bold text-slate-600 mb-1">접점의 $x$좌표 $t$ 조절</label>
                        <input type="range" id="t-slider" min="-1.8" max="1.8" step="0.1" value="0.5" class="w-full accent-indigo-600 cursor-pointer">
                        <div class="flex justify-between text-xs text-slate-500 mt-1">
                            <span>t = -1.8</span>
                            <span id="t-val" class="font-bold text-indigo-600 text-sm">t = 0.5</span>
                            <span>t = 1.8</span>
                        </div>
                    </div>
                    <div class="p-3 bg-slate-50 rounded-xl space-y-2 text-xs border border-slate-200">
                        <div class="flex justify-between">
                            <span class="text-slate-600">접점 좌표:</span>
                            <span id="pt-val" class="font-bold text-slate-800">(0.50, -1.38)</span>
                        </div>
                        <div class="flex justify-between">
                            <span class="text-slate-600">접선의 기울기:</span>
                            <span id="tan-slope" class="font-bold text-rose-600">-2.25</span>
                        </div>
                        <div class="flex justify-between border-t border-slate-200 pt-2">
                            <span class="text-slate-600">접선의 방정식:</span>
                            <span id="tan-eqn" class="font-black text-indigo-600 text-xs">y = -2.25x - 0.25</span>
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
                    <span class="px-2.5 py-1 rounded bg-rose-100 text-rose-700 text-xs font-bold">예제 1 (곡선 밖의 점에서 그은 접선)</span>
                    <button onclick="toggleSolution('sol-ex9-1')" class="text-xs font-bold text-indigo-600 hover:underline">풀이 확인</button>
                </div>
                <h4 class="font-bold text-slate-900 text-base">
                    점 $(0, -4)$에서 곡선 $y = x^2$ 에 그은 접선의 방정식을 모두 구하시오.
                </h4>
                <div id="sol-ex9-1" class="hidden p-4 rounded-xl bg-white border border-slate-200 text-sm space-y-2">
                    <p class="text-slate-700">접점을 $(t, t^2)$이라 하면 $y' = 2x$이므로 접선의 기울기는 $2t$입니다.</p>
                    <p class="font-semibold text-slate-900">$$y - t^2 = 2t(x - t) \\implies y = 2tx - t^2$$</p>
                    <p class="text-slate-700">이 직선이 점 $(0, -4)$를 지나므로 대입하면:</p>
                    <p class="font-semibold text-slate-900">$$-4 = -t^2 \\implies t^2 = 4 \\implies t = \\pm 2$$</p>
                    <p class="font-bold text-emerald-600">따라서 구하는 접선의 방정식은 $y = 4x - 4$ 및 $y = -4x - 4$ 입니다.</p>
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
                    <p class="font-bold text-sm mb-2 text-slate-900">01. 곡선 $y = x^2 - 3x + 2$ 위의 점 $(2, 0)$에서의 접선의 기울기는?</p>
                    <div class="flex items-center gap-2">
                        <button onclick="toggleSolution('ans-9-01')" class="px-3 py-1 bg-teal-600 hover:bg-teal-700 text-white rounded-lg text-xs font-bold transition">정답 확인</button>
                        <span id="ans-9-01" class="hidden font-bold text-sm text-teal-700">$y' = 2x - 3 \\implies 2(2) - 3 = 1$</span>
                    </div>
                </div>
                <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
                    <p class="font-bold text-sm mb-2 text-slate-900">02. 곡선 $y = x^3 + 2$에 접하고 기울기가 3인 접선의 $y$절편은?</p>
                    <div class="flex items-center gap-2">
                        <button onclick="toggleSolution('ans-9-02')" class="px-3 py-1 bg-teal-600 hover:bg-teal-700 text-white rounded-lg text-xs font-bold transition">정답 확인</button>
                        <span id="ans-9-02" class="hidden font-bold text-sm text-teal-700">$3x^2 = 3 \\implies x = \\pm 1$. $x=1$일 때 $(1, 3) \\implies y = 3x$; $x=-1$일 때 $(-1, 1) \\implies y = 3x + 4$. 절편은 $0$ 또는 $4$</span>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <script>
    const cv9 = document.getElementById('tan-canvas');
    if (cv9) {{
        const ctx = cv9.getContext('2d');
        const s = document.getElementById('t-slider');
        const tVal = document.getElementById('t-val');
        const ptVal = document.getElementById('pt-val');
        const tanSlope = document.getElementById('tan-slope');
        const tanEqn = document.getElementById('tan-eqn');

        function f(x) {{ return x * x * x - 3 * x; }}
        function df(x) {{ return 3 * x * x - 3; }}

        function draw9() {{
            const t = parseFloat(s.value);
            const ft = f(t);
            const m = df(t);
            const c = ft - m * t;

            tVal.textContent = 't = ' + t.toFixed(2);
            ptVal.textContent = '(' + t.toFixed(2) + ', ' + ft.toFixed(2) + ')';
            tanSlope.textContent = m.toFixed(2);
            tanEqn.textContent = 'y = ' + m.toFixed(2) + 'x ' + (c >= 0 ? '+ ' : '- ') + Math.abs(c).toFixed(2);

            ctx.clearRect(0, 0, cv9.width, cv9.height);
            const ox = 250, oy = 130, sx = 80, sy = 35;

            // Axes
            ctx.strokeStyle = '#94a3b8';
            ctx.lineWidth = 1.5;
            ctx.beginPath();
            ctx.moveTo(20, oy); ctx.lineTo(480, oy);
            ctx.moveTo(ox, 10); ctx.lineTo(ox, 240);
            ctx.stroke();

            // Cubic curve
            ctx.strokeStyle = '#0284c7';
            ctx.lineWidth = 2.5;
            ctx.beginPath();
            for(let px = -2.2; px <= 2.2; px += 0.05) {{
                const py = f(px);
                const cx = ox + px * sx;
                const cy = oy - py * sy;
                if(px === -2.2) ctx.moveTo(cx, cy);
                else ctx.lineTo(cx, cy);
            }}
            ctx.stroke();

            // Tangent line
            ctx.strokeStyle = '#ef4444';
            ctx.lineWidth = 2;
            ctx.beginPath();
            const x1 = t - 1.5, y1 = m * x1 + c;
            const x2 = t + 1.5, y2 = m * x2 + c;
            ctx.moveTo(ox + x1 * sx, oy - y1 * sy);
            ctx.lineTo(ox + x2 * sx, oy - y2 * sy);
            ctx.stroke();

            // Tangent point
            ctx.fillStyle = '#10b981';
            ctx.beginPath();
            ctx.arc(ox + t * sx, oy - ft * sy, 6, 0, Math.PI * 2);
            ctx.fill();
        }}
        s.addEventListener('input', draw9);
        draw9();
    }}
    </script>
    """

    html = get_header(title, page) + body + get_footer()
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Created:", filename)


def create_unit_10():
    title = "Ⅱ. 미분 - 05. 평균값정리"
    page = "73 ~ 78쪽"
    filename = "2. 미분 5. 평균값정리.html"

    body = f"""
    <header class="lg:hidden fixed top-0 left-0 right-0 h-16 bg-white/95 backdrop-blur border-b border-slate-200 z-40 flex items-center justify-between px-4">
        <span class="font-bold text-lg text-indigo-600">05. 평균값정리</span>
        <button onclick="toggleWhiteboard()" class="px-2.5 py-1.5 rounded-lg bg-indigo-600 text-white text-xs font-bold flex items-center gap-1">
            <i class="fa-solid fa-chalkboard-user"></i> 칠판
        </button>
    </header>

    <aside id="sidebar" class="fixed top-0 left-0 bottom-0 w-72 bg-white border-r border-slate-200 z-40 flex flex-col justify-between shadow-lg lg:shadow-none">
        <div class="p-5 border-b border-slate-200">
            <span class="text-xs font-extrabold tracking-wider uppercase px-2.5 py-1 rounded-md bg-indigo-100 text-indigo-700">Ⅱ. 미분</span>
            <h1 class="text-2xl font-extrabold text-slate-900 mt-2 flex items-center gap-2">
                <i class="fa-solid fa-arrows-split-up-and-left text-indigo-600"></i>
                <span>05. 평균값정리</span>
            </h1>
            <p class="text-xs text-slate-500 mt-1">교과서 {page}</p>
        </div>
        <nav class="flex-1 overflow-y-auto py-3 px-2 space-y-1">
            <a href="#sec-intro" class="nav-link active flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-lightbulb text-amber-500"></i><span>성취기준 & 생각 열기</span>
            </a>
            <a href="#sec-concept1" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-circle-dot text-indigo-500"></i><span>1. 롤의 정리 (Rolle's Theorem)</span>
            </a>
            <a href="#sec-concept2" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-arrow-trend-up text-emerald-500"></i><span>2. 평균값 정리 (MVT)</span>
            </a>
            <a href="#sec-lab" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-sliders text-sky-500"></i><span>평균값 정리 접선 일치 실험실</span>
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
                롤의 정리와 평균값 정리를 이해한다
            </h2>
            <div class="bg-indigo-50/70 rounded-xl p-5 border border-indigo-100">
                <h3 class="font-bold text-indigo-900 text-base mb-2">💡 생각 열기 : 고속도로 평균 속도가 100km/h였다면?</h3>
                <p class="text-sm text-slate-700 leading-relaxed">
                    2시간 동안 200km를 달렸다면 평균 속도는 100km/h입니다. 운전하는 도중 계기판 바늘이 정확히 100km/h를 가리킨 순간이 적어도 한 번은 있었을까요?
                </p>
                <div class="mt-3 flex items-center gap-3">
                    <button onclick="toggleSolution('intro-ans10')" class="text-xs font-bold text-indigo-600 hover:underline">정답 확인</button>
                    <span id="intro-ans10" class="hidden text-xs font-bold text-emerald-600">네! 평균값 정리에 의해 순간 속도(미분계수)가 평균 속도와 같아지는 순간이 반드시 존재합니다.</span>
                </div>
            </div>
        </section>

        <section id="sec-concept1" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center gap-2.5 pb-3 border-b border-slate-200">
                <span class="w-2.5 h-6 bg-indigo-600 rounded-full"></span>
                <h3 class="text-xl font-bold text-slate-900">1. 롤의 정리 (Rolle's Theorem)</h3>
            </div>
            <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                <p class="text-sm text-slate-800 leading-relaxed">
                    함수 $f(x)$가 <b>닫힌구간 $[a, b]$에서 연속</b>이고 <b>열린구간 $(a, b)$에서 미분가능</b>할 때,
                </p>
                <div class="p-4 bg-white rounded-xl border border-indigo-200 text-center font-bold text-indigo-700 text-base">
                    $$f(a) = f(b) \\implies f'(c) = 0 \\quad \\text{{인 }} c \\in (a, b) \\text{{ 가 적어도 하나 존재한다.}}$$
                </div>
                <p class="text-xs text-slate-500">기하학적으로 양 끝점의 높이가 같으면 그 사이에 접선의 기울기가 0(수평 접선)인 점이 적어도 하나 있습니다.</p>
            </div>
        </section>

        <section id="sec-concept2" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center gap-2.5 pb-3 border-b border-slate-200">
                <span class="w-2.5 h-6 bg-emerald-600 rounded-full"></span>
                <h3 class="text-xl font-bold text-slate-900">2. 평균값 정리 (Mean Value Theorem)</h3>
            </div>
            <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                <p class="text-sm text-slate-800 leading-relaxed">
                    함수 $f(x)$가 <b>닫힌구간 $[a, b]$에서 연속</b>이고 <b>열린구간 $(a, b)$에서 미분가능</b>할 때,
                </p>
                <div class="p-4 bg-white rounded-xl border border-emerald-200 text-center font-bold text-emerald-800 text-base">
                    $$\\frac{{f(b) - f(a)}}{{b - a}} = f'(c) \\quad \\text{{인 }} c \\in (a, b) \\text{{ 가 적어도 하나 존재한다.}}$$
                </div>
                <p class="text-xs text-slate-500">기하학적으로 두 점 $A, B$를 잇는 할선과 <b>평행한 접선</b>을 갖는 점 $c$가 $(a, b)$에 적어도 하나 존재합니다.</p>
            </div>
        </section>

        <!-- Section Interactive Lab -->
        <section id="sec-lab" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center justify-between pb-3 border-b border-slate-200">
                <div class="flex items-center gap-2.5">
                    <span class="w-2.5 h-6 bg-sky-600 rounded-full"></span>
                    <h3 class="text-xl font-bold text-slate-900">평균값 정리 $c$의 탐색 시뮬레이터</h3>
                </div>
                <span class="text-xs font-bold text-sky-600 bg-sky-50 px-2.5 py-1 rounded-full border border-sky-200">f(x) = -0.5x² + 2x</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-center">
                <div class="md:col-span-2 bg-slate-50 rounded-xl p-4 flex flex-col items-center border border-slate-200">
                    <canvas id="mvt-canvas" width="500" height="260" class="w-full h-56 rounded-lg bg-white shadow-inner"></canvas>
                </div>
                <div class="space-y-4">
                    <div>
                        <label class="block text-xs font-bold text-slate-600 mb-1">구간 끝점 $b$ 조절 ($a = 0$ 고정)</label>
                        <input type="range" id="b-mvt-slider" min="1.0" max="4.0" step="0.2" value="3.0" class="w-full accent-emerald-600 cursor-pointer">
                        <div class="flex justify-between text-xs text-slate-500 mt-1">
                            <span>b = 1.0</span>
                            <span id="b-mvt-val" class="font-bold text-emerald-600 text-sm">b = 3.0</span>
                            <span>b = 4.0</span>
                        </div>
                    </div>
                    <div class="p-3 bg-slate-50 rounded-xl space-y-2 text-xs border border-slate-200">
                        <div class="flex justify-between">
                            <span class="text-slate-600">할선의 기울기:</span>
                            <span id="mvt-avg-slope" class="font-bold text-sky-600">0.50</span>
                        </div>
                        <div class="flex justify-between border-t border-slate-200 pt-2">
                            <span class="text-slate-600">만족하는 $c$의 값:</span>
                            <span id="mvt-c-val" class="font-black text-rose-600 text-sm">c = 1.50</span>
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
                    <span class="px-2.5 py-1 rounded bg-rose-100 text-rose-700 text-xs font-bold">예제 1 (평균값 정리를 만족하는 c)</span>
                    <button onclick="toggleSolution('sol-ex10-1')" class="text-xs font-bold text-indigo-600 hover:underline">풀이 확인</button>
                </div>
                <h4 class="font-bold text-slate-900 text-base">
                    함수 $f(x) = x^2 - 4x + 3$ 에 대하여 닫힌구간 $[1, 4]$에서 평균값 정리를 만족시키는 상수 $c$의 값을 구하시오.
                </h4>
                <div id="sol-ex10-1" class="hidden p-4 rounded-xl bg-white border border-slate-200 text-sm space-y-2">
                    <p class="text-slate-700">$f(1) = 0$, $f(4) = 16 - 16 + 3 = 3$.</p>
                    <p class="font-semibold text-slate-900">$$\\frac{{f(4) - f(1)}}{{4 - 1}} = \\frac{{3 - 0}}{{3}} = 1$$</p>
                    <p class="text-slate-700">$f'(x) = 2x - 4$ 이므로 $f'(c) = 2c - 4 = 1 \\implies 2c = 5 \\implies c = \\frac{{5}}{{2}} = 2.5$.</p>
                    <p class="font-bold text-emerald-600">$c = 2.5$는 열린구간 $(1, 4)$에 속하므로 올바른 답입니다.</p>
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
                    <p class="font-bold text-sm mb-2 text-slate-900">01. 함수 $f(x) = 4 - x^2$에 대하여 닫힌구간 $[-2, 2]$에서 롤의 정리를 만족하는 $c$의 값은?</p>
                    <div class="flex items-center gap-2">
                        <button onclick="toggleSolution('ans-10-01')" class="px-3 py-1 bg-teal-600 hover:bg-teal-700 text-white rounded-lg text-xs font-bold transition">정답 확인</button>
                        <span id="ans-10-01" class="hidden font-bold text-sm text-teal-700">$f'(c) = -2c = 0 \\implies c = 0$</span>
                    </div>
                </div>
                <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
                    <p class="font-bold text-sm mb-2 text-slate-900">02. 모든 실수에서 $f'(x) = 0$이면 $f(x)$는 어떤 함수인가?</p>
                    <div class="flex items-center gap-2">
                        <button onclick="toggleSolution('ans-10-02')" class="px-3 py-1 bg-teal-600 hover:bg-teal-700 text-white rounded-lg text-xs font-bold transition">정답 확인</button>
                        <span id="ans-10-02" class="hidden font-bold text-sm text-teal-700">상수함수 (평균값 정리의 귀결)</span>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <script>
    const cv10 = document.getElementById('mvt-canvas');
    if (cv10) {{
        const ctx = cv10.getContext('2d');
        const s = document.getElementById('b-mvt-slider');
        const bVal = document.getElementById('b-mvt-val');
        const avgSlope = document.getElementById('mvt-avg-slope');
        const cVal = document.getElementById('mvt-c-val');

        function f(x) {{ return -0.5 * x * x + 2 * x; }}
        function df(x) {{ return -x + 2; }}

        function draw10() {{
            const a = 0.0;
            const b = parseFloat(s.value);
            const fa = f(a);
            const fb = f(b);
            const m = (fb - fa) / (b - a);
            const c = 2 - m; // -c + 2 = m => c = 2 - m

            bVal.textContent = 'b = ' + b.toFixed(1);
            avgSlope.textContent = m.toFixed(2);
            cVal.textContent = 'c = ' + c.toFixed(2);

            ctx.clearRect(0, 0, cv10.width, cv10.height);
            const ox = 70, oy = 210, sx = 90, sy = 55;

            // Axes
            ctx.strokeStyle = '#94a3b8';
            ctx.lineWidth = 1.5;
            ctx.beginPath();
            ctx.moveTo(20, oy); ctx.lineTo(470, oy);
            ctx.moveTo(ox, 10); ctx.lineTo(ox, 240);
            ctx.stroke();

            // Parabola
            ctx.strokeStyle = '#0284c7';
            ctx.lineWidth = 2.5;
            ctx.beginPath();
            for(let px = 0; px <= 4.2; px += 0.05) {{
                const py = f(px);
                const cx = ox + px * sx;
                const cy = oy - py * sy;
                if(px === 0) ctx.moveTo(cx, cy);
                else ctx.lineTo(cx, cy);
            }}
            ctx.stroke();

            // Secant AB
            ctx.strokeStyle = '#6366f1';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(ox + a * sx, oy - fa * sy);
            ctx.lineTo(ox + b * sx, oy - fb * sy);
            ctx.stroke();

            // Tangent at c
            const fc = f(c);
            ctx.strokeStyle = '#ef4444';
            ctx.lineWidth = 2;
            ctx.setLineDash([4, 4]);
            ctx.beginPath();
            const lx1 = c - 1.0, ly1 = fc - m * 1.0;
            const lx2 = c + 1.0, ly2 = fc + m * 1.0;
            ctx.moveTo(ox + lx1 * sx, oy - ly1 * sy);
            ctx.lineTo(ox + lx2 * sx, oy - ly2 * sy);
            ctx.stroke();
            ctx.setLineDash([]);

            // Points
            ctx.fillStyle = '#6366f1';
            ctx.beginPath();
            ctx.arc(ox + a * sx, oy - fa * sy, 5, 0, Math.PI * 2);
            ctx.arc(ox + b * sx, oy - fb * sy, 5, 0, Math.PI * 2);
            ctx.fill();

            ctx.fillStyle = '#ef4444';
            ctx.beginPath();
            ctx.arc(ox + c * sx, oy - fc * sy, 6, 0, Math.PI * 2);
            ctx.fill();
        }}
        s.addEventListener('input', draw10);
        draw10();
    }}
    </script>
    """

    html = get_header(title, page) + body + get_footer()
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Created:", filename)


def create_unit_11():
    title = "Ⅱ. 미분 - 06. 함수의 증가와 감소, 극대와 극소"
    page = "79 ~ 86쪽"
    filename = "2. 미분 6. 함수의 증가와 감소, 극대와 극소.html"

    body = f"""
    <header class="lg:hidden fixed top-0 left-0 right-0 h-16 bg-white/95 backdrop-blur border-b border-slate-200 z-40 flex items-center justify-between px-4">
        <span class="font-bold text-lg text-indigo-600">06. 증가·감소, 극대·극소</span>
        <button onclick="toggleWhiteboard()" class="px-2.5 py-1.5 rounded-lg bg-indigo-600 text-white text-xs font-bold flex items-center gap-1">
            <i class="fa-solid fa-chalkboard-user"></i> 칠판
        </button>
    </header>

    <aside id="sidebar" class="fixed top-0 left-0 bottom-0 w-72 bg-white border-r border-slate-200 z-40 flex flex-col justify-between shadow-lg lg:shadow-none">
        <div class="p-5 border-b border-slate-200">
            <span class="text-xs font-extrabold tracking-wider uppercase px-2.5 py-1 rounded-md bg-indigo-100 text-indigo-700">Ⅱ. 미분</span>
            <h1 class="text-2xl font-extrabold text-slate-900 mt-2 flex items-center gap-2">
                <i class="fa-solid fa-chart-area text-indigo-600"></i>
                <span>06. 증감 & 극대극소</span>
            </h1>
            <p class="text-xs text-slate-500 mt-1">교과서 {page}</p>
        </div>
        <nav class="flex-1 overflow-y-auto py-3 px-2 space-y-1">
            <a href="#sec-intro" class="nav-link active flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-lightbulb text-amber-500"></i><span>성취기준 & 생각 열기</span>
            </a>
            <a href="#sec-concept1" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-arrow-trend-up text-indigo-500"></i><span>1. 함수의 증가와 감소 판정</span>
            </a>
            <a href="#sec-concept2" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-mountain-sun text-emerald-500"></i><span>2. 극대와 극소의 정의 및 판정</span>
            </a>
            <a href="#sec-lab" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-sliders text-sky-500"></i><span>증감표 & 극값 인터랙티브 실험실</span>
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
                함수의 증가와 감소, 극대와 극소를 판정할 수 있다
            </h2>
            <div class="bg-indigo-50/70 rounded-xl p-5 border border-indigo-100">
                <h3 class="font-bold text-indigo-900 text-base mb-2">💡 생각 열기 : 비행기가 최고 고도에 도달했을 때의 수직 속도는?</h3>
                <p class="text-sm text-slate-700 leading-relaxed">
                    상승하던 비행기가 하강으로 전환하는 정상 지점에서는 순간적으로 수직 속도가 $0$이 됩니다. 함수의 그래프에서도 증가에서 감소로 바뀌는 정점(극대)에서 도함수의 값은 얼마일까요?
                </p>
                <div class="mt-3 flex items-center gap-3">
                    <button onclick="toggleSolution('intro-ans11')" class="text-xs font-bold text-indigo-600 hover:underline">정답 확인</button>
                    <span id="intro-ans11" class="hidden text-xs font-bold text-emerald-600">미분가능한 함수라면 $f'(a) = 0$이 되고, 부호가 양수에서 음수로 바뀝니다!</span>
                </div>
            </div>
        </section>

        <section id="sec-concept1" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center gap-2.5 pb-3 border-b border-slate-200">
                <span class="w-2.5 h-6 bg-indigo-600 rounded-full"></span>
                <h3 class="text-xl font-bold text-slate-900">1. 도함수의 부호와 함수의 증가·감소</h3>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="p-4 bg-emerald-50/70 rounded-xl border border-emerald-200 space-y-2">
                    <h4 class="font-bold text-emerald-900 text-sm flex items-center gap-1.5">
                        <i class="fa-solid fa-arrow-trend-up text-emerald-600"></i> 함수 $f(x)$가 증가
                    </h4>
                    <p class="text-xs text-slate-700">열린구간의 모든 $x$에서 <b>$f'(x) > 0$</b> 이면 $f(x)$는 그 구간에서 증가한다.</p>
                </div>
                <div class="p-4 bg-rose-50/70 rounded-xl border border-rose-200 space-y-2">
                    <h4 class="font-bold text-rose-900 text-sm flex items-center gap-1.5">
                        <i class="fa-solid fa-arrow-trend-down text-rose-600"></i> 함수 $f(x)$가 감소
                    </h4>
                    <p class="text-xs text-slate-700">열린구간의 모든 $x$에서 <b>$f'(x) < 0$</b> 이면 $f(x)$는 그 구간에서 감소한다.</p>
                </div>
            </div>
        </section>

        <section id="sec-concept2" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center gap-2.5 pb-3 border-b border-slate-200">
                <span class="w-2.5 h-6 bg-emerald-600 rounded-full"></span>
                <h3 class="text-xl font-bold text-slate-900">2. 극대와 극소의 정의 및 판정</h3>
            </div>
            <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-4">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div class="p-4 bg-white rounded-xl border border-slate-200">
                        <h4 class="font-bold text-indigo-700 text-sm mb-1">⛰️ 극댓값 (Local Maximum)</h4>
                        <p class="text-xs text-slate-600">$x=a$의 좌우에서 $f'(x)$의 부호가 <b>양(+)에서 음(-)</b>으로 변할 때 $f(a)$는 극댓값.</p>
                    </div>
                    <div class="p-4 bg-white rounded-xl border border-slate-200">
                        <h4 class="font-bold text-sky-700 text-sm mb-1">🌊 극솟값 (Local Minimum)</h4>
                        <p class="text-xs text-slate-600">$x=b$의 좌우에서 $f'(x)$의 부호가 <b>음(-)에서 양(+)</b>으로 변할 때 $f(b)$는 극솟값.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Section Interactive Lab -->
        <section id="sec-lab" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center justify-between pb-3 border-b border-slate-200">
                <div class="flex items-center gap-2.5">
                    <span class="w-2.5 h-6 bg-sky-600 rounded-full"></span>
                    <h3 class="text-xl font-bold text-slate-900">3차함수 극대·극소 실시간 탐색기</h3>
                </div>
                <span class="text-xs font-bold text-sky-600 bg-sky-50 px-2.5 py-1 rounded-full border border-sky-200">f(x) = x³ - 3x</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-center">
                <div class="md:col-span-2 bg-slate-50 rounded-xl p-4 flex flex-col items-center border border-slate-200">
                    <canvas id="extrema-canvas" width="500" height="260" class="w-full h-56 rounded-lg bg-white shadow-inner"></canvas>
                </div>
                <div class="space-y-4">
                    <div class="p-4 bg-white rounded-xl border border-slate-200 space-y-3 text-xs">
                        <div class="p-2 bg-indigo-50 rounded border border-indigo-100">
                            <span class="font-bold text-indigo-900">극댓점:</span> (-1, 2) [f'(-1) = 0]
                        </div>
                        <div class="p-2 bg-sky-50 rounded border border-sky-100">
                            <span class="font-bold text-sky-900">극솟점:</span> (1, -2) [f'(1) = 0]
                        </div>
                        <p class="text-slate-500">구간 $(-\\infty, -1)$ 및 $(1, \\infty)$에서는 증가($f'>0$), 구간 $(-1, 1)$에서는 감소($f'<0$).</p>
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
                    <span class="px-2.5 py-1 rounded bg-rose-100 text-rose-700 text-xs font-bold">예제 1 (극값 구하기)</span>
                    <button onclick="toggleSolution('sol-ex11-1')" class="text-xs font-bold text-indigo-600 hover:underline">풀이 확인</button>
                </div>
                <h4 class="font-bold text-slate-900 text-base">
                    함수 $f(x) = 2x^3 - 3x^2 - 12x + 1$ 의 극값을 구하시오.
                </h4>
                <div id="sol-ex11-1" class="hidden p-4 rounded-xl bg-white border border-slate-200 text-sm space-y-2">
                    <p class="text-slate-700">$f'(x) = 6x^2 - 6x - 12 = 6(x^2 - x - 2) = 6(x+1)(x-2)$.</p>
                    <p class="text-slate-700">$f'(x) = 0$인 $x = -1, 2$.</p>
                    <p class="font-semibold text-slate-900">• $x = -1$에서 극댓값: $f(-1) = 2(-1) - 3(1) - 12(-1) + 1 = 8$.</p>
                    <p class="font-semibold text-slate-900">• $x = 2$에서 극솟값: $f(2) = 2(8) - 3(4) - 12(2) + 1 = -19$.</p>
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
                    <p class="font-bold text-sm mb-2 text-slate-900">01. 함수 $f(x) = x^3 - 3x^2$이 감소하는 구간은?</p>
                    <div class="flex items-center gap-2">
                        <button onclick="toggleSolution('ans-11-01')" class="px-3 py-1 bg-teal-600 hover:bg-teal-700 text-white rounded-lg text-xs font-bold transition">정답 확인</button>
                        <span id="ans-11-01" class="hidden font-bold text-sm text-teal-700">$f'(x) = 3x(x-2) < 0 \\implies (0, 2)$</span>
                    </div>
                </div>
                <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
                    <p class="font-bold text-sm mb-2 text-slate-900">02. 3차함수가 극값을 가질 조건은 도함수 $f'(x)=0$의 판별식 $D$가 어떠해야 하는가?</p>
                    <div class="flex items-center gap-2">
                        <button onclick="toggleSolution('ans-11-02')" class="px-3 py-1 bg-teal-600 hover:bg-teal-700 text-white rounded-lg text-xs font-bold transition">정답 확인</button>
                        <span id="ans-11-02" class="hidden font-bold text-sm text-teal-700">$D > 0$ (서로 다른 두 실근을 가져야 부호 변화 발생)</span>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <script>
    const cv11 = document.getElementById('extrema-canvas');
    if (cv11) {{
        const ctx = cv11.getContext('2d');
        const ox = 250, oy = 130, sx = 80, sy = 40;

        function f(x) {{ return x * x * x - 3 * x; }}

        // Axes
        ctx.strokeStyle = '#94a3b8';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(20, oy); ctx.lineTo(480, oy);
        ctx.moveTo(ox, 10); ctx.lineTo(ox, 240);
        ctx.stroke();

        // Cubic Curve
        ctx.strokeStyle = '#0284c7';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        for(let px = -2.2; px <= 2.2; px += 0.05) {{
            const py = f(px);
            const cx = ox + px * sx;
            const cy = oy - py * sy;
            if(px === -2.2) ctx.moveTo(cx, cy);
            else ctx.lineTo(cx, cy);
        }}
        ctx.stroke();

        // Local max at (-1, 2)
        ctx.fillStyle = '#6366f1';
        ctx.beginPath();
        ctx.arc(ox - 1 * sx, oy - 2 * sy, 6, 0, Math.PI * 2);
        ctx.fill();
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('극대 (-1, 2)', ox - 1 * sx - 30, oy - 2 * sy - 10);

        // Local min at (1, -2)
        ctx.fillStyle = '#0ea5e9';
        ctx.beginPath();
        ctx.arc(ox + 1 * sx, oy - (-2) * sy, 6, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillText('극소 (1, -2)', ox + 1 * sx - 10, oy - (-2) * sy + 18);
    }}
    </script>
    """

    html = get_header(title, page) + body + get_footer()
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Created:", filename)


def create_unit_12():
    title = "Ⅱ. 미분 - 07. 함수의 그래프"
    page = "87 ~ 92쪽"
    filename = "2. 미분 7. 함수의 그래프.html"

    body = f"""
    <header class="lg:hidden fixed top-0 left-0 right-0 h-16 bg-white/95 backdrop-blur border-b border-slate-200 z-40 flex items-center justify-between px-4">
        <span class="font-bold text-lg text-indigo-600">07. 함수의 그래프</span>
        <button onclick="toggleWhiteboard()" class="px-2.5 py-1.5 rounded-lg bg-indigo-600 text-white text-xs font-bold flex items-center gap-1">
            <i class="fa-solid fa-chalkboard-user"></i> 칠판
        </button>
    </header>

    <aside id="sidebar" class="fixed top-0 left-0 bottom-0 w-72 bg-white border-r border-slate-200 z-40 flex flex-col justify-between shadow-lg lg:shadow-none">
        <div class="p-5 border-b border-slate-200">
            <span class="text-xs font-extrabold tracking-wider uppercase px-2.5 py-1 rounded-md bg-indigo-100 text-indigo-700">Ⅱ. 미분</span>
            <h1 class="text-2xl font-extrabold text-slate-900 mt-2 flex items-center gap-2">
                <i class="fa-solid fa-bezier-curve text-indigo-600"></i>
                <span>07. 함수의 그래프</span>
            </h1>
            <p class="text-xs text-slate-500 mt-1">교과서 {page}</p>
        </div>
        <nav class="flex-1 overflow-y-auto py-3 px-2 space-y-1">
            <a href="#sec-intro" class="nav-link active flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-lightbulb text-amber-500"></i><span>성취기준 & 생각 열기</span>
            </a>
            <a href="#sec-concept1" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-pen-ruler text-indigo-500"></i><span>1. 다항함수 그래프 그리는 단계</span>
            </a>
            <a href="#sec-concept2" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-arrows-up-down text-emerald-500"></i><span>2. 닫힌구간에서의 최대·최소</span>
            </a>
            <a href="#sec-lab" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-sliders text-sky-500"></i><span>다항함수 계수 조절 인터랙티브 실험실</span>
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
                도함수를 활용하여 함수의 그래프의 개형을 그리고 최대·최소를 구할 수 있다
            </h2>
            <div class="bg-indigo-50/70 rounded-xl p-5 border border-indigo-100">
                <h3 class="font-bold text-indigo-900 text-base mb-2">💡 생각 열기 : 점들을 무수히 찍지 않고도 전체 모양을 그리는 비결?</h3>
                <p class="text-sm text-slate-700 leading-relaxed">
                    도함수 $f'(x)$를 구하면 함수의 기울기가 어디서 양수이고 음수인지, 어디서 꺾이는지(극값)를 한눈에 파악할 수 있어 복잡한 고차함수의 그래프도 정확하게 그릴 수 있습니다.
                </p>
                <div class="mt-3 flex items-center gap-3">
                    <button onclick="toggleSolution('intro-ans12')" class="text-xs font-bold text-indigo-600 hover:underline">정답 확인</button>
                    <span id="intro-ans12" class="hidden text-xs font-bold text-emerald-600">증감표를 작성하여 극값과 축 교점만 잡으면 개형이 완성됩니다!</span>
                </div>
            </div>
        </section>

        <section id="sec-concept1" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center gap-2.5 pb-3 border-b border-slate-200">
                <span class="w-2.5 h-6 bg-indigo-600 rounded-full"></span>
                <h3 class="text-xl font-bold text-slate-900">1. 함수의 그래프 개형을 그리는 4단계</h3>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-4 gap-3">
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-center">
                    <span class="w-6 h-6 rounded-full bg-indigo-600 text-white font-bold text-xs inline-flex items-center justify-center mb-1">1</span>
                    <h4 class="font-bold text-slate-900 text-xs mb-1">도함수 계산</h4>
                    <p class="text-[11px] text-slate-600">$f'(x)$를 구함</p>
                </div>
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-center">
                    <span class="w-6 h-6 rounded-full bg-indigo-600 text-white font-bold text-xs inline-flex items-center justify-center mb-1">2</span>
                    <h4 class="font-bold text-slate-900 text-xs mb-1">극값 후보</h4>
                    <p class="text-[11px] text-slate-600">$f'(x) = 0$ 풀기</p>
                </div>
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-center">
                    <span class="w-6 h-6 rounded-full bg-indigo-600 text-white font-bold text-xs inline-flex items-center justify-center mb-1">3</span>
                    <h4 class="font-bold text-slate-900 text-xs mb-1">증감표 작성</h4>
                    <p class="text-[11px] text-slate-600">부호와 극값 정리</p>
                </div>
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-center">
                    <span class="w-6 h-6 rounded-full bg-indigo-600 text-white font-bold text-xs inline-flex items-center justify-center mb-1">4</span>
                    <h4 class="font-bold text-slate-900 text-xs mb-1">개형 스케치</h4>
                    <p class="text-[11px] text-slate-600">절편과 곡선 연결</p>
                </div>
            </div>
        </section>

        <section id="sec-concept2" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center gap-2.5 pb-3 border-b border-slate-200">
                <span class="w-2.5 h-6 bg-emerald-600 rounded-full"></span>
                <h3 class="text-xl font-bold text-slate-900">2. 닫힌구간 $[a, b]$에서의 최대·최소 구하기</h3>
            </div>
            <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                <p class="text-xs text-slate-700 leading-relaxed">
                    닫힌구간 $[a, b]$에서 연속함수 $f(x)$의 최댓값과 최솟값은 다음 후보들 중 가장 큰 값과 가장 작은 값입니다:
                </p>
                <div class="p-3 bg-white rounded-lg border border-slate-200 text-xs font-bold text-slate-800 flex justify-around">
                    <span>① 구간 안의 모든 극댓값</span>
                    <span>② 구간 안의 모든 극솟값</span>
                    <span>③ 양 끝값 $f(a), f(b)$</span>
                </div>
            </div>
        </section>

        <!-- Section Interactive Lab -->
        <section id="sec-lab" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center justify-between pb-3 border-b border-slate-200">
                <div class="flex items-center gap-2.5">
                    <span class="w-2.5 h-6 bg-sky-600 rounded-full"></span>
                    <h3 class="text-xl font-bold text-slate-900">3차함수 $f(x) = x^3 - 3ax$ 개형 조절기</h3>
                </div>
                <span class="text-xs font-bold text-sky-600 bg-sky-50 px-2.5 py-1 rounded-full border border-sky-200">a 파라미터 조작</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-center">
                <div class="md:col-span-2 bg-slate-50 rounded-xl p-4 flex flex-col items-center border border-slate-200">
                    <canvas id="poly-canvas" width="500" height="260" class="w-full h-56 rounded-lg bg-white shadow-inner"></canvas>
                </div>
                <div class="space-y-4">
                    <div>
                        <label class="block text-xs font-bold text-slate-600 mb-1">상수 $a$ 조절</label>
                        <input type="range" id="a-slider" min="-1.0" max="2.0" step="0.2" value="1.0" class="w-full accent-indigo-600 cursor-pointer">
                        <div class="flex justify-between text-xs text-slate-500 mt-1">
                            <span>a = -1.0</span>
                            <span id="a-val" class="font-bold text-indigo-600 text-sm">a = 1.0</span>
                            <span>a = 2.0</span>
                        </div>
                    </div>
                    <div class="p-3 bg-slate-50 rounded-xl space-y-2 text-xs border border-slate-200">
                        <div class="flex justify-between">
                            <span class="text-slate-600">도함수:</span>
                            <span id="df-eqn" class="font-bold text-slate-800">f'(x) = 3x² - 3</span>
                        </div>
                        <div class="flex justify-between border-t border-slate-200 pt-2">
                            <span class="text-slate-600">개형 상태:</span>
                            <span id="poly-status" class="font-black text-emerald-600 text-sm">극대/극소 2개 존재</span>
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
                    <span class="px-2.5 py-1 rounded bg-rose-100 text-rose-700 text-xs font-bold">예제 1 (최댓값과 최솟값)</span>
                    <button onclick="toggleSolution('sol-ex12-1')" class="text-xs font-bold text-indigo-600 hover:underline">풀이 확인</button>
                </div>
                <h4 class="font-bold text-slate-900 text-base">
                    닫힌구간 $[-1, 3]$에서 함수 $f(x) = 2x^3 - 3x^2 - 12x + 5$ 의 최댓값과 최솟값을 구하시오.
                </h4>
                <div id="sol-ex12-1" class="hidden p-4 rounded-xl bg-white border border-slate-200 text-sm space-y-2">
                    <p class="text-slate-700">$f'(x) = 6x^2 - 6x - 12 = 6(x+1)(x-2) = 0 \\implies x = -1, 2$ (모두 구간 $[-1, 3]$에 포함).</p>
                    <p class="font-semibold text-slate-900">• $f(-1) = 2(-1) - 3(1) - 12(-1) + 5 = 12$ (극대이자 끝값)</p>
                    <p class="font-semibold text-slate-900">• $f(2) = 16 - 12 - 24 + 5 = -15$ (극소)</p>
                    <p class="font-semibold text-slate-900">• $f(3) = 54 - 27 - 36 + 5 = -4$ (끝값)</p>
                    <p class="font-bold text-emerald-600">따라서 최댓값은 $12$, 최솟값은 $-15$ 입니다.</p>
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
                    <p class="font-bold text-sm mb-2 text-slate-900">01. 함수 $f(x) = x^4 - 4x + 1$의 최솟값은?</p>
                    <div class="flex items-center gap-2">
                        <button onclick="toggleSolution('ans-12-01')" class="px-3 py-1 bg-teal-600 hover:bg-teal-700 text-white rounded-lg text-xs font-bold transition">정답 확인</button>
                        <span id="ans-12-01" class="hidden font-bold text-sm text-teal-700">$f'(x) = 4(x^3 - 1) = 0 \\implies x=1$에서 극소이자 최소: $f(1) = -2$</span>
                    </div>
                </div>
                <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
                    <p class="font-bold text-sm mb-2 text-slate-900">02. 3차함수의 그래프가 $x$축과 서로 다른 세 점에서 만날 조건은 (극댓값) $\\times$ (극솟값)의 부호가 어떠해야 하는가?</p>
                    <div class="flex items-center gap-2">
                        <button onclick="toggleSolution('ans-12-02')" class="px-3 py-1 bg-teal-600 hover:bg-teal-700 text-white rounded-lg text-xs font-bold transition">정답 확인</button>
                        <span id="ans-12-02" class="hidden font-bold text-sm text-teal-700">음수 (극댓값 > 0, 극솟값 < 0 이어야 함)</span>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <script>
    const cv12 = document.getElementById('poly-canvas');
    if (cv12) {{
        const ctx = cv12.getContext('2d');
        const s = document.getElementById('a-slider');
        const aVal = document.getElementById('a-val');
        const dfEqn = document.getElementById('df-eqn');
        const status = document.getElementById('poly-status');

        function draw12() {{
            const a = parseFloat(s.value);
            aVal.textContent = 'a = ' + a.toFixed(1);
            dfEqn.textContent = 'f\'(x) = 3x² ' + (a >= 0 ? '- ' + (3*a).toFixed(1) : '+ ' + Math.abs(3*a).toFixed(1));

            if (a > 0.05) {{
                status.textContent = '극대/극소 2개 존재';
                status.className = 'font-black text-emerald-600 text-sm';
            }} else if (Math.abs(a) <= 0.05) {{
                status.textContent = '삼중근 (변곡점 수평접선)';
                status.className = 'font-black text-indigo-600 text-sm';
            }} else {{
                status.textContent = '극값 없음 (단조증가)';
                status.className = 'font-black text-sky-600 text-sm';
            }}

            ctx.clearRect(0, 0, cv12.width, cv12.height);
            const ox = 250, oy = 130, sx = 70, sy = 25;

            // Axes
            ctx.strokeStyle = '#94a3b8';
            ctx.lineWidth = 1.5;
            ctx.beginPath();
            ctx.moveTo(20, oy); ctx.lineTo(480, oy);
            ctx.moveTo(ox, 10); ctx.lineTo(ox, 240);
            ctx.stroke();

            // Curve f(x) = x^3 - 3ax
            ctx.strokeStyle = '#0284c7';
            ctx.lineWidth = 2.5;
            ctx.beginPath();
            for(let px = -2.4; px <= 2.4; px += 0.05) {{
                const py = px * px * px - 3 * a * px;
                const cx = ox + px * sx;
                const cy = oy - py * sy;
                if(px === -2.4) ctx.moveTo(cx, cy);
                else ctx.lineTo(cx, cy);
            }}
            ctx.stroke();
        }}
        s.addEventListener('input', draw12);
        draw12();
    }}
    </script>
    """

    html = get_header(title, page) + body + get_footer()
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Created:", filename)


if __name__ == '__main__':
    create_unit_9()
    create_unit_10()
    create_unit_11()
    create_unit_12()
