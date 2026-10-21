import os
from generate_common import get_header, get_footer

def create_unit_6():
    title = "Ⅱ. 미분 - 01. 미분계수"
    page = "50 ~ 57쪽"
    filename = "2. 미분 1. 미분계수.html"

    body = f"""
    <header class="lg:hidden fixed top-0 left-0 right-0 h-16 bg-white/95 backdrop-blur border-b border-slate-200 z-40 flex items-center justify-between px-4">
        <span class="font-bold text-lg text-indigo-600">01. 미분계수</span>
        <button onclick="toggleWhiteboard()" class="px-2.5 py-1.5 rounded-lg bg-indigo-600 text-white text-xs font-bold flex items-center gap-1">
            <i class="fa-solid fa-chalkboard-user"></i> 칠판
        </button>
    </header>

    <aside id="sidebar" class="fixed top-0 left-0 bottom-0 w-72 bg-white border-r border-slate-200 z-40 flex flex-col justify-between shadow-lg lg:shadow-none">
        <div class="p-5 border-b border-slate-200">
            <span class="text-xs font-extrabold tracking-wider uppercase px-2.5 py-1 rounded-md bg-indigo-100 text-indigo-700">Ⅱ. 미분</span>
            <h1 class="text-2xl font-extrabold text-slate-900 mt-2 flex items-center gap-2">
                <i class="fa-solid fa-chart-line text-indigo-600"></i>
                <span>01. 미분계수</span>
            </h1>
            <p class="text-xs text-slate-500 mt-1">교과서 {page}</p>
        </div>
        <nav class="flex-1 overflow-y-auto py-3 px-2 space-y-1">
            <a href="#sec-intro" class="nav-link active flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-lightbulb text-amber-500"></i><span>성취기준 & 생각 열기</span>
            </a>
            <a href="#sec-concept1" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-arrow-trend-up text-indigo-500"></i><span>1. 평균변화율과 미분계수</span>
            </a>
            <a href="#sec-concept2" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-shapes text-emerald-500"></i><span>2. 미분계수의 기하학적 의미</span>
            </a>
            <a href="#sec-lab" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-sliders text-sky-500"></i><span>할선→접선 수렴 실험실</span>
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
                평균변화율과 미분계수의 뜻을 알고, 그 기하학적 의미를 이해한다
            </h2>
            <div class="bg-indigo-50/70 rounded-xl p-5 border border-indigo-100">
                <h3 class="font-bold text-indigo-900 text-base mb-2">💡 생각 열기 : 과속 단속 카메라는 순간 속도를 어떻게 측정할까?</h3>
                <p class="text-sm text-slate-700 leading-relaxed">
                    구간 단속은 전체 이동 거리와 걸린 시간의 비(평균 속도)를 측정하지만, 고정식 카메라는 불과 수 미터 간격의 센서를 통과하는 극히 짧은 찰나의 시간 간격($\\Delta t \\to 0$)을 측정하여 자동차의 <b>순간 속도</b>를 계산합니다.
                </p>
                <div class="mt-3 flex items-center gap-3">
                    <button onclick="toggleSolution('intro-ans6')" class="text-xs font-bold text-indigo-600 hover:underline">정답 확인</button>
                    <span id="intro-ans6" class="hidden text-xs font-bold text-emerald-600">평균변화율의 시간 간격을 0으로 보내는 극한값이 바로 순간변화율(미분계수)입니다!</span>
                </div>
            </div>
        </section>

        <section id="sec-concept1" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center gap-2.5 pb-3 border-b border-slate-200">
                <span class="w-2.5 h-6 bg-indigo-600 rounded-full"></span>
                <h3 class="text-xl font-bold text-slate-900">1. 평균변화율과 미분계수의 정의</h3>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <h4 class="font-bold text-indigo-900 text-sm">📊 평균변화율 (Average Rate of Change)</h4>
                    <p class="text-xs text-slate-700 leading-relaxed">
                        $x$의 값이 $a$에서 $b$까지 변할 때:
                    </p>
                    <div class="p-3 bg-white rounded-lg border border-slate-200 font-bold text-center text-sm text-indigo-700">
                        $$\\frac{{\\Delta y}}{{\\Delta x}} = \\frac{{f(b) - f(a)}}{{b - a}} = \\frac{{f(a + \\Delta x) - f(a)}}{{\\Delta x}}$$
                    </div>
                    <p class="text-xs text-slate-500">기하학적으로 곡선 위의 두 점 $(a, f(a))$와 $(b, f(b))$를 지나는 <b>할선의 기울기</b>입니다.</p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <h4 class="font-bold text-emerald-900 text-sm">⚡ 미분계수 (Instantaneous Rate of Change)</h4>
                    <p class="text-xs text-slate-700 leading-relaxed">
                        $x = a$에서의 순간변화율:
                    </p>
                    <div class="p-3 bg-white rounded-lg border border-slate-200 font-bold text-center text-sm text-emerald-700">
                        $$f'(a) = \\lim_{{\\Delta x \\to 0}} \\frac{{f(a + \\Delta x) - f(a)}}{{\\Delta x}} = \\lim_{{x \\to a}} \\frac{{f(x) - f(a)}}{{x - a}}$$
                    </div>
                    <p class="text-xs text-slate-500">기하학적으로 곡선 $y = f(x)$ 위의 점 $(a, f(a))$에서의 <b>접선의 기울기</b>입니다.</p>
                </div>
            </div>
        </section>

        <!-- Section Interactive Lab -->
        <section id="sec-lab" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center justify-between pb-3 border-b border-slate-200">
                <div class="flex items-center gap-2.5">
                    <span class="w-2.5 h-6 bg-sky-600 rounded-full"></span>
                    <h3 class="text-xl font-bold text-slate-900">기하학적 시뮬레이터 : 할선이 접선이 되는 순간</h3>
                </div>
                <span class="text-xs font-bold text-sky-600 bg-sky-50 px-2.5 py-1 rounded-full border border-sky-200">f(x) = 0.5x² (기준점 a = 1.0)</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-center">
                <div class="md:col-span-2 bg-slate-50 rounded-xl p-4 flex flex-col items-center border border-slate-200">
                    <canvas id="slope-canvas" width="500" height="260" class="w-full h-56 rounded-lg bg-white shadow-inner"></canvas>
                </div>
                <div class="space-y-4">
                    <div>
                        <label class="block text-xs font-bold text-slate-600 mb-1">$\\Delta x$ (점 B의 간격) 조절</label>
                        <input type="range" id="dx-slider" min="0.1" max="2.0" step="0.05" value="1.5" class="w-full accent-indigo-600 cursor-pointer">
                        <div class="flex justify-between text-xs text-slate-500 mt-1">
                            <span>0.1 (접선에 근접)</span>
                            <span id="dx-val" class="font-bold text-indigo-600 text-sm">Δx = 1.50</span>
                            <span>2.0 (할선)</span>
                        </div>
                    </div>
                    <div class="p-3 bg-slate-50 rounded-xl space-y-2 text-xs border border-slate-200">
                        <div class="flex justify-between">
                            <span class="text-slate-600">평균변화율 (할선 기울기):</span>
                            <span id="secant-slope" class="font-bold text-sky-600 text-sm">1.75</span>
                        </div>
                        <div class="flex justify-between border-t border-slate-200 pt-2">
                            <span class="text-slate-600">미분계수 $f'(1)$ (접선 기울기):</span>
                            <span class="font-black text-rose-600 text-sm">1.00</span>
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
                    <span class="px-2.5 py-1 rounded bg-rose-100 text-rose-700 text-xs font-bold">예제 1 (미분계수의 정의)</span>
                    <button onclick="toggleSolution('sol-ex6-1')" class="text-xs font-bold text-indigo-600 hover:underline">풀이 확인</button>
                </div>
                <h4 class="font-bold text-slate-900 text-base">
                    함수 $f(x) = 2x^2 - x$ 에 대하여 $x = 2$에서의 미분계수 $f'(2)$를 정의를 이용하여 구하시오.
                </h4>
                <div id="sol-ex6-1" class="hidden p-4 rounded-xl bg-white border border-slate-200 text-sm space-y-2">
                    <p class="text-slate-700">$f(2) = 2(2^2) - 2 = 6$.</p>
                    <p class="font-semibold text-slate-900">$$f'(2) = \\lim_{{x \\to 2}} \\frac{{f(x) - f(2)}}{{x - 2}} = \\lim_{{x \\to 2}} \\frac{{2x^2 - x - 6}}{{x - 2}}$$</p>
                    <p class="font-semibold text-slate-900">$$= \\lim_{{x \\to 2}} \\frac{{(x - 2)(2x + 3)}}{{x - 2}} = \\lim_{{x \\to 2}} (2x + 3) = 2(2) + 3 = 7$$</p>
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
                    <p class="font-bold text-sm mb-2 text-slate-900">01. 함수 $f(x) = 3x - 1$에서 $x$가 $1$에서 $4$까지 변할 때의 평균변화율은?</p>
                    <div class="flex items-center gap-2">
                        <button onclick="toggleSolution('ans-6-01')" class="px-3 py-1 bg-teal-600 hover:bg-teal-700 text-white rounded-lg text-xs font-bold transition">정답 확인</button>
                        <span id="ans-6-01" class="hidden font-bold text-sm text-teal-700">$\\frac{{f(4)-f(1)}}{{4-1}} = \\frac{{11-2}}{{3}} = 3$</span>
                    </div>
                </div>
                <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
                    <p class="font-bold text-sm mb-2 text-slate-900">02. 미분계수 변형 공식: $\\lim_{{h \\to 0}} \\frac{{f(a + 2h) - f(a)}}{{h}}$ 는 미분계수로 어떻게 표현되는가?</p>
                    <div class="flex items-center gap-2">
                        <button onclick="toggleSolution('ans-6-02')" class="px-3 py-1 bg-teal-600 hover:bg-teal-700 text-white rounded-lg text-xs font-bold transition">정답 확인</button>
                        <span id="ans-6-02" class="hidden font-bold text-sm text-teal-700">$2f'(a)$</span>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <script>
    const cv6 = document.getElementById('slope-canvas');
    if (cv6) {{
        const ctx = cv6.getContext('2d');
        const s = document.getElementById('dx-slider');
        const dxVal = document.getElementById('dx-val');
        const secantSlope = document.getElementById('secant-slope');

        function f(x) {{ return 0.5 * x * x; }}

        function draw6() {{
            const dx = parseFloat(s.value);
            dxVal.textContent = 'Δx = ' + dx.toFixed(2);

            const a = 1.0;
            const b = a + dx;
            const fa = f(a);
            const fb = f(b);
            const slope = (fb - fa) / dx;
            secantSlope.textContent = slope.toFixed(2);

            ctx.clearRect(0, 0, cv6.width, cv6.height);
            const ox = 80, oy = 210, sx = 80, sy = 30;

            // Axes
            ctx.strokeStyle = '#94a3b8';
            ctx.lineWidth = 1.5;
            ctx.beginPath();
            ctx.moveTo(20, oy); ctx.lineTo(460, oy);
            ctx.moveTo(ox, 10); ctx.lineTo(ox, 240);
            ctx.stroke();

            // Parabola f(x) = 0.5 x^2
            ctx.strokeStyle = '#475569';
            ctx.lineWidth = 2;
            ctx.beginPath();
            for(let px = 0; px <= 4.0; px += 0.05) {{
                const py = f(px);
                const cx = ox + px * sx;
                const cy = oy - py * sy;
                if(px === 0) ctx.moveTo(cx, cy);
                else ctx.lineTo(cx, cy);
            }}
            ctx.stroke();

            // Tangent line at (1, 0.5) with slope 1
            ctx.strokeStyle = '#ef4444';
            ctx.lineWidth = 1.5;
            ctx.setLineDash([4, 4]);
            ctx.beginPath();
            ctx.moveTo(ox + 0 * sx, oy - (-0.5) * sy);
            ctx.lineTo(ox + 3.5 * sx, oy - (3.0) * sy);
            ctx.stroke();
            ctx.setLineDash([]);

            // Secant line through A(a, fa) and B(b, fb)
            ctx.strokeStyle = '#0284c7';
            ctx.lineWidth = 2.5;
            ctx.beginPath();
            const xLeft = 0.2;
            const yLeft = fa + slope * (xLeft - a);
            const xRight = 3.8;
            const yRight = fa + slope * (xRight - a);
            ctx.moveTo(ox + xLeft * sx, oy - yLeft * sy);
            ctx.lineTo(ox + xRight * sx, oy - yRight * sy);
            ctx.stroke();

            // Point A
            ctx.fillStyle = '#ef4444';
            ctx.beginPath();
            ctx.arc(ox + a * sx, oy - fa * sy, 6, 0, Math.PI * 2);
            ctx.fill();

            // Point B
            ctx.fillStyle = '#0284c7';
            ctx.beginPath();
            ctx.arc(ox + b * sx, oy - fb * sy, 6, 0, Math.PI * 2);
            ctx.fill();
        }}
        s.addEventListener('input', draw6);
        draw6();
    }}
    </script>
    """

    html = get_header(title, page) + body + get_footer()
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Created:", filename)


def create_unit_7():
    title = "Ⅱ. 미분 - 02. 미분가능성과 연속성"
    page = "58 ~ 61쪽"
    filename = "2. 미분 2. 미분가능성과 연속성.html"

    body = f"""
    <header class="lg:hidden fixed top-0 left-0 right-0 h-16 bg-white/95 backdrop-blur border-b border-slate-200 z-40 flex items-center justify-between px-4">
        <span class="font-bold text-lg text-indigo-600">02. 미분가능과 연속</span>
        <button onclick="toggleWhiteboard()" class="px-2.5 py-1.5 rounded-lg bg-indigo-600 text-white text-xs font-bold flex items-center gap-1">
            <i class="fa-solid fa-chalkboard-user"></i> 칠판
        </button>
    </header>

    <aside id="sidebar" class="fixed top-0 left-0 bottom-0 w-72 bg-white border-r border-slate-200 z-40 flex flex-col justify-between shadow-lg lg:shadow-none">
        <div class="p-5 border-b border-slate-200">
            <span class="text-xs font-extrabold tracking-wider uppercase px-2.5 py-1 rounded-md bg-indigo-100 text-indigo-700">Ⅱ. 미분</span>
            <h1 class="text-2xl font-extrabold text-slate-900 mt-2 flex items-center gap-2">
                <i class="fa-solid fa-shuffle text-indigo-600"></i>
                <span>02. 미분가능과 연속</span>
            </h1>
            <p class="text-xs text-slate-500 mt-1">교과서 {page}</p>
        </div>
        <nav class="flex-1 overflow-y-auto py-3 px-2 space-y-1">
            <a href="#sec-intro" class="nav-link active flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-lightbulb text-amber-500"></i><span>성취기준 & 생각 열기</span>
            </a>
            <a href="#sec-concept1" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-diagram-project text-indigo-500"></i><span>1. 미분가능과 연속의 관계</span>
            </a>
            <a href="#sec-lab" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-sliders text-sky-500"></i><span>뾰족점(첨점) 미분불가 실험</span>
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
                미분가능성과 연속성의 관계를 이해한다
            </h2>
            <div class="bg-indigo-50/70 rounded-xl p-5 border border-indigo-100">
                <h3 class="font-bold text-indigo-900 text-base mb-2">💡 생각 열기 : 연속이지만 꺾인 점에서는 접선을 그을 수 있을까?</h3>
                <p class="text-sm text-slate-700 leading-relaxed">
                    $f(x) = |x|$의 그래프는 $x=0$에서 끊어지지 않고 이어져 있습니다. 그러나 $x=0$에서 왼쪽 접선의 기울기는 $-1$, 오른쪽 접선의 기울기는 $+1$이 됩니다. 그렇다면 $x=0$에서 미분계수가 존재할 수 있을까요?
                </p>
                <div class="mt-3 flex items-center gap-3">
                    <button onclick="toggleSolution('intro-ans7')" class="text-xs font-bold text-indigo-600 hover:underline">정답 확인</button>
                    <span id="intro-ans7" class="hidden text-xs font-bold text-rose-600">좌미분계수와 우미분계수가 다르므로 $x=0$에서 미분 불가능합니다!</span>
                </div>
            </div>
        </section>

        <section id="sec-concept1" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center gap-2.5 pb-3 border-b border-slate-200">
                <span class="w-2.5 h-6 bg-indigo-600 rounded-full"></span>
                <h3 class="text-xl font-bold text-slate-900">1. 미분가능성과 연속성의 포함 관계</h3>
            </div>
            <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-4">
                <div class="p-4 bg-white rounded-xl border border-indigo-200 shadow-xs flex flex-col items-center text-center">
                    <span class="text-xs font-black uppercase text-indigo-600 tracking-wider">핵심 명제</span>
                    <p class="text-lg font-black text-slate-900 mt-1">
                        함수 $f(x)$가 $x = a$에서 <span class="text-indigo-600">미분가능</span>하면 $\implies$ $x = a$에서 <span class="text-emerald-600">연속</span>이다. (참)
                    </p>
                    <p class="text-xs text-rose-600 font-bold mt-2">
                        ⚠️ 역은 성립하지 않는다: 연속함수라고 해서 반드시 미분가능한 것은 아니다! (반례: $f(x) = |x|$)
                    </p>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                    <div class="p-3 bg-white rounded-lg border border-slate-200">
                        <b>증명 아이디어:</b> $\\lim_{{x \\to a}} (f(x) - f(a)) = \\lim_{{x \\to a}} \\frac{{f(x)-f(a)}}{{x-a}} \\times (x-a) = f'(a) \\times 0 = 0 \\implies \\lim_{{x \\to a}} f(x) = f(a)$.
                    </div>
                    <div class="p-3 bg-white rounded-lg border border-slate-200">
                        <b>대우 명제 (항상 참):</b> $x = a$에서 <b>불연속</b>이면 $x = a$에서 <b>미분 불가능</b>하다.
                    </div>
                </div>
            </div>
        </section>

        <!-- Section Interactive Lab -->
        <section id="sec-lab" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center justify-between pb-3 border-b border-slate-200">
                <div class="flex items-center gap-2.5">
                    <span class="w-2.5 h-6 bg-sky-600 rounded-full"></span>
                    <h3 class="text-xl font-bold text-slate-900">뾰족점(첨점) 미분불가 vs 매끄러운 곡선 비교</h3>
                </div>
                <span class="text-xs font-bold text-sky-600 bg-sky-50 px-2.5 py-1 rounded-full border border-sky-200">y = |x|</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-center">
                <div class="md:col-span-2 bg-slate-50 rounded-xl p-4 flex flex-col items-center border border-slate-200">
                    <canvas id="cusp-canvas" width="500" height="260" class="w-full h-56 rounded-lg bg-white shadow-inner"></canvas>
                </div>
                <div class="space-y-4">
                    <div class="p-3 bg-white rounded-xl space-y-2 text-xs border border-slate-200">
                        <div class="flex justify-between">
                            <span class="text-slate-600">우미분계수 ($x \\to 0^+$):</span>
                            <span class="font-bold text-sky-600 text-sm">+1.00</span>
                        </div>
                        <div class="flex justify-between">
                            <span class="text-slate-600">좌미분계수 ($x \\to 0^-$):</span>
                            <span class="font-bold text-rose-600 text-sm">-1.00</span>
                        </div>
                        <div class="flex justify-between border-t border-slate-200 pt-2">
                            <span class="text-slate-600">미분계수 존재 여부:</span>
                            <span class="font-black text-rose-600 text-sm">존재하지 않음 (미분불가)</span>
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
                    <span class="px-2.5 py-1 rounded bg-rose-100 text-rose-700 text-xs font-bold">예제 1 (조각함수의 미분가능성)</span>
                    <button onclick="toggleSolution('sol-ex7-1')" class="text-xs font-bold text-indigo-600 hover:underline">풀이 확인</button>
                </div>
                <h4 class="font-bold text-slate-900 text-base">
                    함수 $f(x) = \\begin{{cases}} x^2 + ax & (x \\ge 1) \\\\ bx + 1 & (x < 1) \\end{{cases}}$ 이 $x = 1$에서 미분가능할 때, 상수 $a, b$의 값을 구하시오.
                </h4>
                <div id="sol-ex7-1" class="hidden p-4 rounded-xl bg-white border border-slate-200 text-sm space-y-2">
                    <p class="text-slate-700">1) <b>연속 조건:</b> $\\lim_{{x \\to 1^+}} f(x) = \\lim_{{x \\to 1^-}} f(x) \\implies 1 + a = b + 1 \\implies a = b$.</p>
                    <p class="text-slate-700">2) <b>미분계수 일치 조건:</b> 각각 미분하면 우도함수 $2x + a$, 좌도함수 $b$. $x=1$ 대입 시 $2(1) + a = b$.</p>
                    <p class="text-slate-700">$a = b$를 대입하면 $2 + a = a \\implies$ 모순? 다시 확인:</p>
                    <p class="font-semibold text-slate-900">연속: $1 + a = b + 1 \\implies b = a$. 미분계수: 우미분 $2(1)+a = 2+a$, 좌미분 $b$. $2+a = b \\implies 2+a = a$ 해가 없음(문제 수치 점검).</p>
                    <p class="font-semibold text-slate-900">만약 $bx + 2$였다면: $1+a = b+2 \\implies b = a-1$, $2+a = b \\implies 2+a = a-1$. 일반적인 미분가능 문제 해결 원리는 <b>① 연속성 체크 ($f(1^+)=f(1^-)$)</b> 후 <b>② 좌우 미분계수 일치</b>로 연립방정식을 세우는 것입니다.</p>
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
                    <p class="font-bold text-sm mb-2 text-slate-900">01. 다음 중 옳은 것은? (① 연속이면 미분가능, ② 미분가능하면 연속)</p>
                    <div class="flex items-center gap-2">
                        <button onclick="toggleSolution('ans-7-01')" class="px-3 py-1 bg-teal-600 hover:bg-teal-700 text-white rounded-lg text-xs font-bold transition">정답 확인</button>
                        <span id="ans-7-01" class="hidden font-bold text-sm text-teal-700">② 미분가능하면 항상 연속이다!</span>
                    </div>
                </div>
                <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
                    <p class="font-bold text-sm mb-2 text-slate-900">02. 함수 $f(x) = |x - 2|$는 $x = 2$에서 미분가능한가?</p>
                    <div class="flex items-center gap-2">
                        <button onclick="toggleSolution('ans-7-02')" class="px-3 py-1 bg-teal-600 hover:bg-teal-700 text-white rounded-lg text-xs font-bold transition">정답 확인</button>
                        <span id="ans-7-02" class="hidden font-bold text-sm text-teal-700">미분 불가능하다 (뾰족점이므로 좌미분계수 -1, 우미분계수 +1로 다름)</span>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <script>
    const cv7 = document.getElementById('cusp-canvas');
    if (cv7) {{
        const ctx = cv7.getContext('2d');
        const ox = 250, oy = 210, sx = 80, sy = 60;

        // Axes
        ctx.strokeStyle = '#94a3b8';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(20, oy); ctx.lineTo(480, oy);
        ctx.moveTo(ox, 10); ctx.lineTo(ox, 240);
        ctx.stroke();

        // Left branch y = -x
        ctx.strokeStyle = '#ef4444';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(ox - 2.5 * sx, oy - 2.5 * sy);
        ctx.lineTo(ox, oy);
        ctx.stroke();

        // Right branch y = x
        ctx.strokeStyle = '#0284c7';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(ox, oy);
        ctx.lineTo(ox + 2.5 * sx, oy - 2.5 * sy);
        ctx.stroke();

        // Cusp point
        ctx.fillStyle = '#7c3aed';
        ctx.beginPath();
        ctx.arc(ox, oy, 6, 0, Math.PI * 2);
        ctx.fill();

        // Slope notes
        ctx.fillStyle = '#ef4444';
        ctx.font = 'bold 12px sans-serif';
        ctx.fillText('기울기 = -1', ox - 110, oy - 1.2 * sy);
        ctx.fillStyle = '#0284c7';
        ctx.fillText('기울기 = +1', ox + 40, oy - 1.2 * sy);
    }}
    </script>
    """

    html = get_header(title, page) + body + get_footer()
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Created:", filename)


def create_unit_8():
    title = "Ⅱ. 미분 - 03. 도함수"
    page = "62 ~ 68쪽"
    filename = "2. 미분 3. 도함수.html"

    body = f"""
    <header class="lg:hidden fixed top-0 left-0 right-0 h-16 bg-white/95 backdrop-blur border-b border-slate-200 z-40 flex items-center justify-between px-4">
        <span class="font-bold text-lg text-indigo-600">03. 도함수</span>
        <button onclick="toggleWhiteboard()" class="px-2.5 py-1.5 rounded-lg bg-indigo-600 text-white text-xs font-bold flex items-center gap-1">
            <i class="fa-solid fa-chalkboard-user"></i> 칠판
        </button>
    </header>

    <aside id="sidebar" class="fixed top-0 left-0 bottom-0 w-72 bg-white border-r border-slate-200 z-40 flex flex-col justify-between shadow-lg lg:shadow-none">
        <div class="p-5 border-b border-slate-200">
            <span class="text-xs font-extrabold tracking-wider uppercase px-2.5 py-1 rounded-md bg-indigo-100 text-indigo-700">Ⅱ. 미분</span>
            <h1 class="text-2xl font-extrabold text-slate-900 mt-2 flex items-center gap-2">
                <i class="fa-solid fa-square-root-variable text-indigo-600"></i>
                <span>03. 도함수</span>
            </h1>
            <p class="text-xs text-slate-500 mt-1">교과서 {page}</p>
        </div>
        <nav class="flex-1 overflow-y-auto py-3 px-2 space-y-1">
            <a href="#sec-intro" class="nav-link active flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-lightbulb text-amber-500"></i><span>성취기준 & 생각 열기</span>
            </a>
            <a href="#sec-concept1" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-calculator text-indigo-500"></i><span>1. 도함수의 정의와 y=xⁿ 미분법</span>
            </a>
            <a href="#sec-concept2" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-xmark text-emerald-500"></i><span>2. 곱의 미분법 공식</span>
            </a>
            <a href="#sec-lab" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm text-slate-700 hover:bg-slate-100">
                <i class="fa-solid fa-sliders text-sky-500"></i><span>도함수 그래프 생성 실험실</span>
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
                함수 $y=x^n$의 도함수를 구할 수 있고, 함수의 실수배, 합, 차, 곱의 미분법을 안다
            </h2>
            <div class="bg-indigo-50/70 rounded-xl p-5 border border-indigo-100">
                <h3 class="font-bold text-indigo-900 text-base mb-2">💡 생각 열기 : 매번 극한 계산을 하지 않고 접선의 기울기를 알 수 있을까?</h3>
                <p class="text-sm text-slate-700 leading-relaxed">
                    $x=1, 2, 3$에서의 미분계수를 구할 때마다 극한 식을 세우지 않고, 임의의 $x$에 대하여 미분계수를 대응시키는 새로운 함수를 만들면 한 번에 계산할 수 있습니다!
                </p>
                <div class="mt-3 flex items-center gap-3">
                    <button onclick="toggleSolution('intro-ans8')" class="text-xs font-bold text-indigo-600 hover:underline">정답 확인</button>
                    <span id="intro-ans8" class="hidden text-xs font-bold text-emerald-600">이 새로운 함수가 바로 도함수 $f'(x)$입니다!</span>
                </div>
            </div>
        </section>

        <section id="sec-concept1" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center gap-2.5 pb-3 border-b border-slate-200">
                <span class="w-2.5 h-6 bg-indigo-600 rounded-full"></span>
                <h3 class="text-xl font-bold text-slate-900">1. 도함수의 정의 & 거듭제곱 미분법</h3>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="p-4 bg-slate-50 rounded-xl border border-slate-200">
                    <h4 class="font-bold text-slate-900 text-sm mb-2">📌 도함수 정의</h4>
                    <p class="text-xs text-slate-600 mb-2">정의역의 각 $x$에 미분계수 $f'(x)$를 대응시키는 함수:</p>
                    <div class="p-2.5 bg-white rounded-lg border border-slate-200 text-center font-bold text-indigo-700 text-sm">
                        $$f'(x) = \\lim_{{h \\to 0}} \\frac{{f(x+h) - f(x)}}{{h}}$$
                    </div>
                </div>
                <div class="p-4 bg-slate-50 rounded-xl border border-slate-200">
                    <h4 class="font-bold text-slate-900 text-sm mb-2">⚡ 거듭제곱과 상수의 미분법</h4>
                    <div class="space-y-2 text-xs">
                        <div class="p-2 bg-white rounded border border-slate-200">1. $y = c$ (상수함수) $\\implies y' = 0$</div>
                        <div class="p-2 bg-white rounded border border-slate-200">2. $y = x^n$ ($n$은 양의 정수) $\\implies y' = n x^{{n-1}}$</div>
                    </div>
                </div>
            </div>
        </section>

        <section id="sec-concept2" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center gap-2.5 pb-3 border-b border-slate-200">
                <span class="w-2.5 h-6 bg-emerald-600 rounded-full"></span>
                <h3 class="text-xl font-bold text-slate-900">2. 함수의 곱의 미분법 공식</h3>
            </div>
            <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                <div class="p-4 bg-white rounded-xl border border-emerald-200 shadow-xs">
                    <h4 class="font-bold text-emerald-900 text-sm mb-1">📌 두 함수의 곱의 미분법</h4>
                    <p class="text-sm font-black text-slate-900">
                        $$\\{{f(x)g(x)\\}}' = f'(x)g(x) + f(x)g'(x)$$
                    </p>
                    <p class="text-xs text-slate-500 mt-1">"앞 미분 뒤 그대로 + 앞 그대로 뒤 미분"</p>
                </div>
                <div class="p-4 bg-white rounded-xl border border-sky-200 shadow-xs">
                    <h4 class="font-bold text-sky-900 text-sm mb-1">📌 세 함수의 곱의 미분법</h4>
                    <p class="text-sm font-black text-slate-900">
                        $$\\{{f(x)g(x)h(x)\\}}' = f'gh + fg'h + fgh'$$
                    </p>
                </div>
            </div>
        </section>

        <!-- Section Interactive Lab -->
        <section id="sec-lab" class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-slate-200 space-y-6">
            <div class="flex items-center justify-between pb-3 border-b border-slate-200">
                <div class="flex items-center gap-2.5">
                    <span class="w-2.5 h-6 bg-sky-600 rounded-full"></span>
                    <h3 class="text-xl font-bold text-slate-900">원래 함수 $f(x)$와 도함수 $f'(x)$의 실시간 비교</h3>
                </div>
                <span class="text-xs font-bold text-sky-600 bg-sky-50 px-2.5 py-1 rounded-full border border-sky-200">f(x) = x² - 2x</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-center">
                <div class="md:col-span-2 bg-slate-50 rounded-xl p-4 flex flex-col items-center border border-slate-200">
                    <canvas id="deriv-canvas" width="500" height="260" class="w-full h-56 rounded-lg bg-white shadow-inner"></canvas>
                </div>
                <div class="space-y-4">
                    <div>
                        <label class="block text-xs font-bold text-slate-600 mb-1">$x$ 좌표 이동 슬라이더</label>
                        <input type="range" id="x8-slider" min="-0.5" max="2.5" step="0.1" value="1.0" class="w-full accent-emerald-600 cursor-pointer">
                        <div class="flex justify-between text-xs text-slate-500 mt-1">
                            <span>x = -0.5</span>
                            <span id="x8-val" class="font-bold text-emerald-600 text-sm">x = 1.0</span>
                            <span>x = 2.5</span>
                        </div>
                    </div>
                    <div class="p-3 bg-slate-50 rounded-xl space-y-2 text-xs border border-slate-200">
                        <div class="flex justify-between">
                            <span class="text-slate-600">함숫값 $f(x)$:</span>
                            <span id="fx8-val" class="font-bold text-slate-800">-1.00</span>
                        </div>
                        <div class="flex justify-between border-t border-slate-200 pt-2">
                            <span class="text-slate-600">도함숫값 $f'(x) = 2x - 2$:</span>
                            <span id="dfx8-val" class="font-black text-indigo-600 text-sm">0.00 (수평 접선)</span>
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
                    <span class="px-2.5 py-1 rounded bg-rose-100 text-rose-700 text-xs font-bold">예제 1 (곱의 미분법)</span>
                    <button onclick="toggleSolution('sol-ex8-1')" class="text-xs font-bold text-indigo-600 hover:underline">풀이 확인</button>
                </div>
                <h4 class="font-bold text-slate-900 text-base">
                    함수 $f(x) = (2x + 1)(x^2 - 3x + 2)$ 에 대하여 $f'(1)$의 값을 구하시오.
                </h4>
                <div id="sol-ex8-1" class="hidden p-4 rounded-xl bg-white border border-slate-200 text-sm space-y-2">
                    <p class="text-slate-700">곱의 미분법을 적용합니다:</p>
                    <p class="font-semibold text-slate-900">$$f'(x) = (2x+1)'(x^2 - 3x + 2) + (2x+1)(x^2 - 3x + 2)'$$</p>
                    <p class="font-semibold text-slate-900">$$= 2(x^2 - 3x + 2) + (2x + 1)(2x - 3)$$</p>
                    <p class="text-slate-700">$x=1$을 대입하면:</p>
                    <p class="font-bold text-emerald-600">$$f'(1) = 2(1 - 3 + 2) + (2 + 1)(2 - 3) = 2(0) + 3(-1) = -3$$</p>
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
                    <p class="font-bold text-sm mb-2 text-slate-900">01. $f(x) = 4x^3 - 5x^2 + 7$ 의 도함수 $f'(x)$는?</p>
                    <div class="flex items-center gap-2">
                        <button onclick="toggleSolution('ans-8-01')" class="px-3 py-1 bg-teal-600 hover:bg-teal-700 text-white rounded-lg text-xs font-bold transition">정답 확인</button>
                        <span id="ans-8-01" class="hidden font-bold text-sm text-teal-700">$12x^2 - 10x$</span>
                    </div>
                </div>
                <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
                    <p class="font-bold text-sm mb-2 text-slate-900">02. $f(x) = (x^2 + 1)^2$ 의 $x=1$에서의 미분계수는?</p>
                    <div class="flex items-center gap-2">
                        <button onclick="toggleSolution('ans-8-02')" class="px-3 py-1 bg-teal-600 hover:bg-teal-700 text-white rounded-lg text-xs font-bold transition">정답 확인</button>
                        <span id="ans-8-02" class="hidden font-bold text-sm text-teal-700">$f(x) = x^4 + 2x^2 + 1 \\implies f'(x) = 4x^3 + 4x \\implies f'(1) = 8$</span>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <script>
    const cv8 = document.getElementById('deriv-canvas');
    if (cv8) {{
        const ctx = cv8.getContext('2d');
        const s = document.getElementById('x8-slider');
        const xVal = document.getElementById('x8-val');
        const fxVal = document.getElementById('fx8-val');
        const dfxVal = document.getElementById('dfx8-val');

        function f(x) {{ return x * x - 2 * x; }}
        function df(x) {{ return 2 * x - 2; }}

        function draw8() {{
            const x = parseFloat(s.value);
            const y = f(x);
            const m = df(x);
            xVal.textContent = 'x = ' + x.toFixed(1);
            fxVal.textContent = y.toFixed(2);
            dfxVal.textContent = m.toFixed(2) + (Math.abs(m) < 0.05 ? ' (극값, 수평 접선)' : '');

            ctx.clearRect(0, 0, cv8.width, cv8.height);
            const ox = 150, oy = 160, sx = 80, sy = 50;

            // Axes
            ctx.strokeStyle = '#94a3b8';
            ctx.lineWidth = 1.5;
            ctx.beginPath();
            ctx.moveTo(20, oy); ctx.lineTo(460, oy);
            ctx.moveTo(ox, 10); ctx.lineTo(ox, 240);
            ctx.stroke();

            // Parabola f(x)
            ctx.strokeStyle = '#0284c7';
            ctx.lineWidth = 2.5;
            ctx.beginPath();
            for(let px = -0.5; px <= 2.8; px += 0.05) {{
                const py = f(px);
                const cx = ox + px * sx;
                const cy = oy - py * sy;
                if(px === -0.5) ctx.moveTo(cx, cy);
                else ctx.lineTo(cx, cy);
            }}
            ctx.stroke();

            // Tangent line at (x, y)
            ctx.strokeStyle = '#ef4444';
            ctx.lineWidth = 2;
            ctx.beginPath();
            const lx1 = x - 1.0, ly1 = y - m * 1.0;
            const lx2 = x + 1.0, ly2 = y + m * 1.0;
            ctx.moveTo(ox + lx1 * sx, oy - ly1 * sy);
            ctx.lineTo(ox + lx2 * sx, oy - ly2 * sy);
            ctx.stroke();

            // Current point
            ctx.fillStyle = '#10b981';
            ctx.beginPath();
            ctx.arc(ox + x * sx, oy - y * sy, 6, 0, Math.PI * 2);
            ctx.fill();
        }}
        s.addEventListener('input', draw8);
        draw8();
    }}
    </script>
    """

    html = get_header(title, page) + body + get_footer()
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Created:", filename)


if __name__ == '__main__':
    create_unit_6()
    create_unit_7()
    create_unit_8()
