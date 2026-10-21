import os

# Common header template
def get_header(unit_title, page_range):
    return f"""<!DOCTYPE html>
<html lang="ko" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{unit_title} | 인터랙티브 수업 자료</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Pretendard Font -->
    <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" />
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
    <!-- KaTeX for Math Rendering -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" />
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>

    <style>
        body {{
            font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif;
            word-break: keep-all;
            overflow-x: hidden;
        }}
        .katex-display {{
            overflow-x: auto;
            overflow-y: hidden;
            padding: 0.5rem 0;
        }}
        .active-nav {{
            background-color: #e0e7ff;
            color: #4338ca;
            font-weight: 700;
            border-right: 4px solid #6366f1;
        }}
        .dark .active-nav {{
            background-color: #312e81;
            color: #c7d2fe;
            border-right: 4px solid #818cf8;
        }}
        /* Drawing Canvas */
        .scratchpad-canvas {{
            touch-action: none;
            cursor: crosshair;
            background-image: radial-gradient(#cbd5e1 1px, transparent 1px);
            background-size: 16px 16px;
        }}
        .dark .scratchpad-canvas {{
            background-image: radial-gradient(#334155 1px, transparent 1px);
        }}
        /* Electronic Whiteboard Overlay */
        #wb-canvas {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 45;
            pointer-events: none;
            touch-action: none;
        }}
        #wb-canvas.wb-drawing-active {{
            pointer-events: auto;
            cursor: crosshair;
        }}
        .wb-color-btn.active {{
            transform: scale(1.2);
            box-shadow: 0 0 0 3px #fff, 0 0 0 5px #4f46e5;
        }}
        .wb-tool-btn.active {{
            background-color: #4f46e5;
            color: #ffffff;
        }}
        #wb-toolbar {{
            z-index: 50;
        }}
        #floating-controls {{
            z-index: 49;
        }}
        @media print {{
            #sidebar, #floating-controls, #wb-toolbar, #wb-canvas, .no-print {{
                display: none !important;
            }}
            #main-content {{
                margin-left: 0 !important;
                width: 100% !important;
            }}
            .solution-box {{
                display: block !important;
            }}
        }}
    </style>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    colors: {{
                        primary: '#4f46e5',
                        secondary: '#0ea5e9',
                    }}
                }}
            }}
        }}
    </script>
</head>
<body class="bg-slate-50 text-slate-800 dark:bg-slate-900 dark:text-slate-100 transition-colors duration-200">

    <!-- Full-screen Electronic Whiteboard Canvas -->
    <canvas id="wb-canvas"></canvas>

    <!-- Electronic Whiteboard Floating Toolbar -->
    <div id="wb-toolbar" class="hidden fixed top-4 left-1/2 -translate-x-1/2 z-50 bg-slate-900/95 text-white backdrop-blur-md px-4 py-2.5 rounded-2xl shadow-2xl border border-slate-700 flex flex-wrap items-center gap-2 sm:gap-3">
        <div class="flex items-center gap-1.5 pr-2 border-r border-slate-700">
            <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
            <span class="text-xs font-extrabold tracking-wide text-sky-300">전자칠판</span>
        </div>

        <div class="flex items-center gap-1 bg-slate-800 p-1 rounded-xl">
            <button id="wb-btn-pointer" onclick="setWbTool('pointer')" class="wb-tool-btn px-2.5 py-1.5 rounded-lg text-xs font-bold transition flex items-center gap-1" title="화면 스크롤 및 버튼 클릭">
                <i class="fa-solid fa-hand-pointer"></i> <span class="hidden sm:inline">조작</span>
            </button>
            <button id="wb-btn-pen" onclick="setWbTool('pen')" class="wb-tool-btn active px-2.5 py-1.5 rounded-lg text-xs font-bold transition flex items-center gap-1" title="일반 펜 판서">
                <i class="fa-solid fa-pen"></i> <span class="hidden sm:inline">펜</span>
            </button>
            <button id="wb-btn-highlighter" onclick="setWbTool('highlighter')" class="wb-tool-btn px-2.5 py-1.5 rounded-lg text-xs font-bold transition flex items-center gap-1" title="형광펜 강조">
                <i class="fa-solid fa-highlighter"></i> <span class="hidden sm:inline">형광펜</span>
            </button>
            <button id="wb-btn-eraser" onclick="setWbTool('eraser')" class="wb-tool-btn px-2.5 py-1.5 rounded-lg text-xs font-bold transition flex items-center gap-1" title="부분 지우개">
                <i class="fa-solid fa-eraser"></i> <span class="hidden sm:inline">지우개</span>
            </button>
        </div>

        <div class="flex items-center gap-2 px-2 border-l border-r border-slate-700">
            <button onclick="setWbColor('#ef4444', this)" class="wb-color-btn active w-5 h-5 rounded-full bg-red-500 transition" title="빨강"></button>
            <button onclick="setWbColor('#3b82f6', this)" class="wb-color-btn w-5 h-5 rounded-full bg-blue-500 transition" title="파랑"></button>
            <button onclick="setWbColor('#10b981', this)" class="wb-color-btn w-5 h-5 rounded-full bg-emerald-500 transition" title="초록"></button>
            <button onclick="setWbColor('#f59e0b', this)" class="wb-color-btn w-5 h-5 rounded-full bg-amber-400 transition" title="노랑"></button>
            <button onclick="setWbColor('#1e293b', this)" class="wb-color-btn w-5 h-5 rounded-full bg-slate-800 border border-white/50 transition" title="검정"></button>
        </div>

        <div class="hidden md:flex items-center gap-2">
            <span class="text-[11px] text-slate-400">굵기</span>
            <input type="range" id="wb-size" min="2" max="14" value="4" class="w-16 accent-indigo-400 cursor-pointer h-1.5 bg-slate-700 rounded-lg">
        </div>

        <div class="flex items-center gap-1.5 pl-1">
            <button onclick="undoWb()" class="p-1.5 px-2.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold transition" title="실행 취소">
                <i class="fa-solid fa-rotate-left"></i>
            </button>
            <button onclick="clearWb()" class="p-1.5 px-2.5 rounded-lg bg-rose-900/70 hover:bg-rose-800 text-rose-200 text-xs font-semibold transition" title="판서 전체 지우기">
                <i class="fa-solid fa-trash-can mr-1"></i>전체 지우기
            </button>
            <button onclick="toggleWhiteboard()" class="p-1.5 px-2.5 rounded-lg bg-slate-700 hover:bg-slate-600 text-xs font-bold transition" title="전자칠판 닫기">
                <i class="fa-solid fa-xmark"></i> 닫기
            </button>
        </div>
    </div>
"""

def get_footer():
    return """
    <!-- Floating Whiteboard & Scroll Controls -->
    <div id="floating-controls" class="fixed bottom-6 right-6 z-40 flex flex-col items-end gap-3 no-print">
        <button onclick="toggleWhiteboard()" title="전자칠판 판서 모드 켜기/끄기"
            class="w-12 h-12 rounded-full bg-indigo-600 hover:bg-indigo-700 text-white shadow-xl flex items-center justify-center ring-4 ring-indigo-500/20 hover:scale-110 active:scale-95 transition-all duration-200 cursor-pointer">
            <i class="fa-solid fa-chalkboard-user text-lg"></i>
        </button>
        <button id="scroll-top-btn" onclick="window.scrollTo({top: 0, behavior: 'smooth'})" title="맨 위로 가기"
            class="w-10 h-10 rounded-full bg-white dark:bg-slate-800 text-slate-600 dark:text-slate-300 shadow-md border border-slate-200 dark:border-slate-700 flex items-center justify-center opacity-0 pointer-events-none translate-y-4 hover:bg-slate-100 dark:hover:bg-slate-700 transition-all duration-200">
            <i class="fa-solid fa-arrow-up text-sm"></i>
        </button>
    </div>

    <!-- Common JavaScript -->
    <script>
    // KaTeX Auto-render
    document.addEventListener("DOMContentLoaded", function() {
        if (typeof renderMathInElement === 'function') {
            renderMathInElement(document.body, {
                delimiters: [
                    {left: '$$', right: '$$', display: true},
                    {left: '$', right: '$', display: false}
                ],
                throwOnError: false
            });
        }
    });

    // Dark Mode Toggle
    function toggleDarkMode() {
        document.documentElement.classList.toggle('dark');
        if (typeof drawSimulation === 'function') drawSimulation();
    }

    // Solution Toggle
    function toggleSolution(id) {
        const box = document.getElementById(id);
        if (box) {
            box.classList.toggle('hidden');
        }
    }

    // Scratchpad canvas initialization
    function initScratchpads() {
        document.querySelectorAll('.scratchpad-canvas').forEach(canvas => {
            const ctx = canvas.getContext('2d');
            let drawing = false;

            function resize() {
                const rect = canvas.getBoundingClientRect();
                if (canvas.width !== rect.width || canvas.height !== rect.height) {
                    canvas.width = rect.width;
                    canvas.height = rect.height;
                }
            }
            resize();
            window.addEventListener('resize', resize);

            function getPos(e) {
                const rect = canvas.getBoundingClientRect();
                const touch = e.touches ? e.touches[0] : e;
                return {
                    x: touch.clientX - rect.left,
                    y: touch.clientY - rect.top
                };
            }

            function start(e) {
                drawing = true;
                ctx.beginPath();
                const p = getPos(e);
                ctx.moveTo(p.x, p.y);
            }
            function move(e) {
                if (!drawing) return;
                e.preventDefault();
                const p = getPos(e);
                ctx.lineWidth = 2;
                ctx.lineCap = 'round';
                ctx.strokeStyle = document.documentElement.classList.contains('dark') ? '#93c5fd' : '#2563eb';
                ctx.lineTo(p.x, p.y);
                ctx.stroke();
            }
            function stop() {
                drawing = false;
            }

            canvas.addEventListener('mousedown', start);
            canvas.addEventListener('mousemove', move);
            window.addEventListener('mouseup', stop);
            canvas.addEventListener('touchstart', start, {passive: false});
            canvas.addEventListener('touchmove', move, {passive: false});
            window.addEventListener('touchend', stop);

            const clearBtn = canvas.parentElement.querySelector('.clear-scratchpad-btn');
            if (clearBtn) {
                clearBtn.addEventListener('click', () => {
                    ctx.clearRect(0, 0, canvas.width, canvas.height);
                });
            }
        });
    }

    // Whiteboard Engine
    let wbActive = false;
    let wbTool = 'pen';
    let wbColor = '#ef4444';
    let wbStrokes = [];
    let wbCurrentStroke = null;
    let wbDrawing = false;

    function initWhiteboard() {
        const canvas = document.getElementById('wb-canvas');
        if (!canvas) return;
        syncWhiteboardHeight();

        if (window.ResizeObserver) {
            const ro = new ResizeObserver(() => syncWhiteboardHeight());
            ro.observe(document.body);
        }

        function getDocPt(e) {
            const touch = e.touches && e.touches[0] ? e.touches[0] : (e.changedTouches && e.changedTouches[0] ? e.changedTouches[0] : e);
            return {
                x: touch.clientX + window.scrollX,
                y: touch.clientY + window.scrollY
            };
        }

        function startDraw(e) {
            if (!wbActive || wbTool === 'pointer') return;
            if (e.button !== undefined && e.button !== 0) return;
            wbDrawing = true;
            const pt = getDocPt(e);
            const sizeInput = document.getElementById('wb-size');
            const size = sizeInput ? parseFloat(sizeInput.value) : 4;

            wbCurrentStroke = {
                tool: wbTool,
                color: wbColor,
                size: size,
                points: [pt]
            };
            wbStrokes.push(wbCurrentStroke);
            redrawWhiteboard();
        }

        function moveDraw(e) {
            if (!wbDrawing || !wbActive || wbTool === 'pointer' || !wbCurrentStroke) return;
            e.preventDefault();
            const pt = getDocPt(e);
            wbCurrentStroke.points.push(pt);
            drawStrokeSegment(wbCurrentStroke);
        }

        function endDraw() {
            if (!wbDrawing) return;
            wbDrawing = false;
            wbCurrentStroke = null;
            redrawWhiteboard();
        }

        canvas.addEventListener('mousedown', startDraw);
        window.addEventListener('mousemove', moveDraw, { passive: false });
        window.addEventListener('mouseup', endDraw);
        canvas.addEventListener('touchstart', startDraw, { passive: false });
        canvas.addEventListener('touchmove', moveDraw, { passive: false });
        window.addEventListener('touchend', endDraw);
    }

    function applyStrokeStyle(ctx, stroke) {
        ctx.lineCap = 'round';
        ctx.lineJoin = 'round';
        if (stroke.tool === 'eraser') {
            ctx.globalCompositeOperation = 'destination-out';
            ctx.lineWidth = stroke.size * 4.5;
            ctx.strokeStyle = 'rgba(0,0,0,1)';
        } else if (stroke.tool === 'highlighter') {
            ctx.globalCompositeOperation = 'source-over';
            ctx.lineWidth = stroke.size * 3.4;
            ctx.strokeStyle = stroke.color + '44';
        } else {
            ctx.globalCompositeOperation = 'source-over';
            ctx.lineWidth = stroke.size;
            ctx.strokeStyle = stroke.color;
        }
    }

    function drawStrokeSegment(stroke) {
        const canvas = document.getElementById('wb-canvas');
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        const pts = stroke.points;
        if (pts.length < 2) return;

        if (stroke.tool === 'highlighter') {
            redrawWhiteboard();
            return;
        }

        ctx.save();
        applyStrokeStyle(ctx, stroke);
        const p1 = pts[pts.length - 2];
        const p2 = pts[pts.length - 1];
        ctx.beginPath();
        ctx.moveTo(p1.x, p1.y);
        ctx.lineTo(p2.x, p2.y);
        ctx.stroke();
        ctx.restore();
    }

    function redrawWhiteboard() {
        const canvas = document.getElementById('wb-canvas');
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        for (const stroke of wbStrokes) {
            if (!stroke.points || stroke.points.length === 0) continue;
            ctx.save();
            applyStrokeStyle(ctx, stroke);
            ctx.beginPath();
            ctx.moveTo(stroke.points[0].x, stroke.points[0].y);
            if (stroke.points.length === 1) {
                ctx.lineTo(stroke.points[0].x + 0.1, stroke.points[0].y + 0.1);
            } else {
                for (let i = 1; i < stroke.points.length; i++) {
                    ctx.lineTo(stroke.points[i].x, stroke.points[i].y);
                }
            }
            ctx.stroke();
            ctx.restore();
        }
    }

    function syncWhiteboardHeight() {
        const canvas = document.getElementById('wb-canvas');
        if (!canvas) return;
        const docWidth = document.documentElement.clientWidth;
        const docHeight = Math.max(
            document.body.scrollHeight,
            document.documentElement.scrollHeight,
            window.innerHeight
        );
        if (canvas.width !== docWidth || Math.abs(canvas.height - docHeight) > 4) {
            canvas.width = docWidth;
            canvas.height = docHeight;
            redrawWhiteboard();
        }
    }

    function toggleWhiteboard() {
        wbActive = !wbActive;
        const toolbar = document.getElementById('wb-toolbar');
        const canvas = document.getElementById('wb-canvas');
        if (wbActive) {
            syncWhiteboardHeight();
            toolbar.classList.remove('hidden');
            setWbTool('pen');
        } else {
            toolbar.classList.add('hidden');
            canvas.classList.remove('wb-drawing-active');
        }
    }

    function setWbTool(tool) {
        wbTool = tool;
        const canvas = document.getElementById('wb-canvas');
        document.querySelectorAll('.wb-tool-btn').forEach(b => b.classList.remove('active'));
        const activeBtn = document.getElementById('wb-btn-' + tool);
        if (activeBtn) activeBtn.classList.add('active');

        if (tool === 'pointer') {
            canvas.classList.remove('wb-drawing-active');
        } else {
            canvas.classList.add('wb-drawing-active');
        }
    }

    function setWbColor(hex, btnEl) {
        wbColor = hex;
        document.querySelectorAll('.wb-color-btn').forEach(b => b.classList.remove('active'));
        if (btnEl) btnEl.classList.add('active');
        if (wbTool === 'pointer' || wbTool === 'eraser') setWbTool('pen');
    }

    function undoWb() {
        if (wbStrokes.length === 0) return;
        wbStrokes.pop();
        redrawWhiteboard();
    }

    function clearWb() {
        wbStrokes = [];
        redrawWhiteboard();
    }

    // Scroll listener for top button and scrollspy
    window.addEventListener('scroll', () => {
        const scrollTopBtn = document.getElementById('scroll-top-btn');
        if (scrollTopBtn) {
            if (window.scrollY > 260) {
                scrollTopBtn.classList.remove('opacity-0', 'pointer-events-none', 'translate-y-4');
                scrollTopBtn.classList.add('opacity-100', 'translate-y-0');
            } else {
                scrollTopBtn.classList.add('opacity-0', 'pointer-events-none', 'translate-y-4');
                scrollTopBtn.classList.remove('opacity-100', 'translate-y-0');
            }
        }
    });

    document.addEventListener('DOMContentLoaded', () => {
        initWhiteboard();
        initScratchpads();
    });
    </script>
</body>
</html>
"""

print("Helper definitions ready.")
