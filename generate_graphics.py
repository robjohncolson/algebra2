"""Generate all Blooket + Google Form graphics for Unit 4 Lesson 1."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

BLOOKET_DIR = 'deliverables/unit4_lesson1/blooket/images'
GFORM_DIR = 'deliverables/unit4_lesson1/google-form/images'

def save(fig, path):
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='white', pad_inches=0.3)
    plt.close(fig)
    print(f'  saved {path}')

# ─── Shared style ───
plt.rcParams.update({
    'font.size': 14,
    'axes.titlesize': 16,
    'axes.labelsize': 13,
    'font.family': 'sans-serif',
})
PURPLE = '#7c3aed'
BLUE = '#2563eb'
RED = '#dc2626'
GREEN = '#16a34a'
GRAY = '#6b7280'
ORANGE = '#ea580c'

# ════════════════════════════════════════════════
# BLOOKET GRAPHICS (12)
# ════════════════════════════════════════════════

# Q1: Inverse variation table — rectangle area 72
def blooket_q1():
    fig, ax = plt.subplots(figsize=(5, 2.5))
    ax.axis('off')
    data = [['Length (x)', '4', '6', '9', '18', '36'],
            ['Width (y)',  '18', '12', '8', '4', '?']]
    tbl = ax.table(cellText=data, loc='center', cellLoc='center')
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(13)
    tbl.scale(1, 1.8)
    for (r,c), cell in tbl.get_celld().items():
        if r == 0:
            cell.set_facecolor(PURPLE)
            cell.set_text_props(color='white', fontweight='bold')
        if c == 0:
            cell.set_text_props(fontweight='bold')
        if r == 1 and c == 5:
            cell.set_facecolor('#fef3c7')
            cell.set_text_props(fontweight='bold', color=RED)
    ax.set_title('Rectangle area = 72 sq in.  Find the missing width.', fontsize=13, pad=12)
    save(fig, f'{BLOOKET_DIR}/q01_table_rect.png')

# Q2: k = 72 highlighted
def blooket_q2():
    fig, ax = plt.subplots(figsize=(5, 2.5))
    ax.axis('off')
    ax.text(0.5, 0.65, r'$x \cdot y = k$', ha='center', va='center', fontsize=28, color=PURPLE)
    ax.text(0.5, 0.35, r'$4 \times 18 = 72$    $6 \times 12 = 72$    $9 \times 8 = 72$',
            ha='center', va='center', fontsize=14, color=GRAY)
    ax.text(0.5, 0.12, 'The product never changes. What is 72 called?',
            ha='center', va='center', fontsize=12, style='italic', color='black')
    save(fig, f'{BLOOKET_DIR}/q02_constant_k.png')

# Q3: y = 1/x graph with horizontal asymptote highlighted
def blooket_q3():
    fig, ax = plt.subplots(figsize=(5, 4))
    x_pos = np.linspace(0.15, 6, 200)
    x_neg = np.linspace(-6, -0.15, 200)
    ax.plot(x_pos, 1/x_pos, color=PURPLE, lw=2.5)
    ax.plot(x_neg, 1/x_neg, color=PURPLE, lw=2.5)
    ax.axhline(0, color=RED, ls='--', lw=2, label='y = 0 (what is this line?)')
    ax.axvline(0, color=GRAY, ls=':', lw=1)
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(r'$y = \frac{1}{x}$', fontsize=18)
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(True, alpha=0.3)
    save(fig, f'{BLOOKET_DIR}/q03_asymptote_hline.png')

# Q4: f(x) = 1/x table showing reciprocal mapping
def blooket_q4():
    fig, ax = plt.subplots(figsize=(5, 2.5))
    ax.axis('off')
    data = [['x',    '2',   '4',    '5',   '10'],
            ['f(x)', '0.5', '0.25', '0.2', '0.1']]
    tbl = ax.table(cellText=data, loc='center', cellLoc='center')
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(14)
    tbl.scale(1, 1.8)
    for (r,c), cell in tbl.get_celld().items():
        if r == 0:
            cell.set_facecolor(BLUE)
            cell.set_text_props(color='white', fontweight='bold')
    ax.set_title('Each output = 1 / input.  What type of function?', fontsize=13, pad=12)
    save(fig, f'{BLOOKET_DIR}/q04_reciprocal_table.png')

# Q5: Car wash inverse variation
def blooket_q5():
    fig, ax = plt.subplots(figsize=(5, 3))
    students = [2, 3, 4, 6, 8]
    time = [48/s for s in students]
    ax.bar(range(len(students)), time, color=[ORANGE if s==3 else BLUE for s in students], width=0.6)
    ax.set_xticks(range(len(students)))
    ax.set_xticklabels([str(s) for s in students])
    ax.set_xlabel('Number of students')
    ax.set_ylabel('Minutes')
    ax.set_title('Car wash time vs. number of students', fontsize=13)
    for i, (s, t) in enumerate(zip(students, time)):
        ax.text(i, t + 0.5, f'{t:.0f}', ha='center', fontsize=11, fontweight='bold')
    save(fig, f'{BLOOKET_DIR}/q05_car_wash_bar.png')

# Q6: k = 48 product diagram
def blooket_q6():
    fig, ax = plt.subplots(figsize=(5, 2.5))
    ax.axis('off')
    ax.text(0.5, 0.7, r'students $\times$ minutes $= k$', ha='center', fontsize=20, color=PURPLE)
    ax.text(0.5, 0.4, r'$3 \times 16 = 48$          $2 \times 24 = 48$',
            ha='center', fontsize=15, color=GRAY)
    ax.text(0.5, 0.15, 'The product 48 is always the same. What is it called?',
            ha='center', fontsize=12, style='italic')
    save(fig, f'{BLOOKET_DIR}/q06_k_product.png')

# Q7: String length vs frequency
def blooket_q7():
    fig, ax = plt.subplots(figsize=(5, 3))
    lengths = np.array([13, 17, 20, 26, 39])
    k = 26 * 330
    freq = k / lengths
    ax.plot(lengths, freq, 'o-', color=PURPLE, lw=2, markersize=8)
    ax.set_xlabel('String length (inches)')
    ax.set_ylabel('Frequency (cycles/sec)')
    ax.set_title('Shorter string → higher pitch', fontsize=13)
    ax.grid(True, alpha=0.3)
    save(fig, f'{BLOOKET_DIR}/q07_string_freq.png')

# Q8: Translated reciprocal with vertical asymptote x=3
def blooket_q8():
    fig, ax = plt.subplots(figsize=(5, 4))
    x1 = np.linspace(3.15, 8, 200)
    x2 = np.linspace(-2, 2.85, 200)
    y1 = 1/(x1-3) + 2
    y2 = 1/(x2-3) + 2
    ax.plot(x1, y1, color=PURPLE, lw=2.5, label=r'$y = \frac{1}{x-3}+2$')
    ax.plot(x2, y2, color=PURPLE, lw=2.5)
    ax.axvline(3, color=RED, ls='--', lw=2, label='x = 3 (what is this?)')
    ax.axhline(2, color=ORANGE, ls='--', lw=1.5, alpha=0.6, label='y = 2')
    ax.set_xlim(-3, 9)
    ax.set_ylim(-6, 10)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Translated reciprocal function', fontsize=14)
    ax.legend(fontsize=10, loc='upper left')
    ax.grid(True, alpha=0.3)
    save(fig, f'{BLOOKET_DIR}/q08_vert_asymptote.png')

# Q9: Parent function y=1/x with labeled points
def blooket_q9():
    fig, ax = plt.subplots(figsize=(5, 4))
    x_pos = np.linspace(0.2, 6, 200)
    x_neg = np.linspace(-6, -0.2, 200)
    ax.plot(x_pos, 1/x_pos, color=PURPLE, lw=2.5)
    ax.plot(x_neg, 1/x_neg, color=PURPLE, lw=2.5)
    pts = [(1,1), (2, 0.5), (0.5, 2), (-1, -1)]
    for px, py in pts:
        ax.plot(px, py, 'o', color=RED, markersize=7)
        ax.annotate(f'({px}, {py})', (px, py), textcoords='offset points',
                    xytext=(10, 5), fontsize=10, color=RED)
    ax.axhline(0, color=GRAY, ls=':', lw=1)
    ax.axvline(0, color=GRAY, ls=':', lw=1)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_title(r'$y = \frac{1}{x}$  — the parent _____ function', fontsize=14)
    ax.grid(True, alpha=0.3)
    save(fig, f'{BLOOKET_DIR}/q09_parent_recip.png')

# Q10: Ice melt — temp vs time
def blooket_q10():
    fig, ax = plt.subplots(figsize=(5, 3))
    temps = np.array([10, 15, 20, 25, 30, 40])
    k = 20 * 20  # 400
    times = k / temps
    ax.plot(temps, times, 's-', color=BLUE, lw=2, markersize=8)
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Melt time (min)')
    ax.set_title('Hotter → melts faster', fontsize=13)
    ax.grid(True, alpha=0.3)
    save(fig, f'{BLOOKET_DIR}/q10_ice_melt.png')

# Q11: y = 1/(x+5) - 4 with horizontal asymptote y = -4
def blooket_q11():
    fig, ax = plt.subplots(figsize=(5, 4))
    x1 = np.linspace(-4.8, 10, 200)
    x2 = np.linspace(-15, -5.2, 200)
    y1 = 1/(x1+5) - 4
    y2 = 1/(x2+5) - 4
    ax.plot(x1, y1, color=PURPLE, lw=2.5, label=r'$y = \frac{1}{x+5} - 4$')
    ax.plot(x2, y2, color=PURPLE, lw=2.5)
    ax.axhline(-4, color=RED, ls='--', lw=2, label='y = −4 (what is this?)')
    ax.axvline(-5, color=GRAY, ls=':', lw=1.5)
    ax.set_xlim(-12, 10)
    ax.set_ylim(-10, 4)
    ax.set_title('What is the dashed red line called?', fontsize=13)
    ax.legend(fontsize=10, loc='upper right')
    ax.grid(True, alpha=0.3)
    save(fig, f'{BLOOKET_DIR}/q11_horiz_asymptote.png')

# Q12: xy = k formula emphasis
def blooket_q12():
    fig, ax = plt.subplots(figsize=(5, 2.5))
    ax.axis('off')
    ax.text(0.5, 0.65, r'$xy = k$', ha='center', va='center', fontsize=40, color=PURPLE, fontweight='bold')
    ax.text(0.5, 0.3, 'In every inverse variation,\nthe letter k represents the ________.',
            ha='center', va='center', fontsize=14, color='black')
    save(fig, f'{BLOOKET_DIR}/q12_xy_equals_k.png')


# ════════════════════════════════════════════════
# GOOGLE FORM GRAPHICS (5)
# ════════════════════════════════════════════════

# GF Q1: Inverse variation table with missing p
def gform_q1():
    fig, ax = plt.subplots(figsize=(6, 2.5))
    ax.axis('off')
    data = [['x', '3', '10', '15', '30'],
            ['y', '5', 'p = ?', '1', '0.5']]
    tbl = ax.table(cellText=data, loc='center', cellLoc='center')
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(15)
    tbl.scale(1, 2)
    for (r,c), cell in tbl.get_celld().items():
        if r == 0:
            cell.set_facecolor(PURPLE)
            cell.set_text_props(color='white', fontweight='bold')
        if r == 1 and c == 2:
            cell.set_facecolor('#fef3c7')
            cell.set_text_props(fontweight='bold', color=RED)
    ax.set_title('This table represents an inverse variation. Find p.', fontsize=14, pad=15)
    save(fig, f'{GFORM_DIR}/q1_table_find_p.png')

# GF Q2: Table for equation matching
def gform_q2():
    fig, ax = plt.subplots(figsize=(6, 2.5))
    ax.axis('off')
    data = [['x', '−3', '−1', '1/2', '2/3'],
            ['y', '4', '12', '−24', '−18']]
    tbl = ax.table(cellText=data, loc='center', cellLoc='center')
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(15)
    tbl.scale(1, 2)
    for (r,c), cell in tbl.get_celld().items():
        if r == 0:
            cell.set_facecolor(BLUE)
            cell.set_text_props(color='white', fontweight='bold')
    ax.set_title('Write an equation for this inverse variation.', fontsize=14, pad=15)
    save(fig, f'{GFORM_DIR}/q2_table_equation.png')

# GF Q3: Car wash visual
def gform_q3():
    fig, ax = plt.subplots(figsize=(6, 3.5))
    students = [1, 2, 3, 4, 6]
    k = 3 * 16  # 48
    time = [k/s for s in students]
    colors = [GRAY, ORANGE, GREEN, GRAY, GRAY]
    bars = ax.bar(range(len(students)), time, color=colors, width=0.6, edgecolor='white', lw=1.5)
    ax.set_xticks(range(len(students)))
    ax.set_xticklabels([f'{s} student{"s" if s>1 else ""}' for s in students], fontsize=10)
    ax.set_ylabel('Minutes to wash car')
    ax.set_title('Time varies inversely with number of students.\n3 students → 16 min. How long for 2 students?', fontsize=12)
    for i, t in enumerate(time):
        label = f'{t:.0f} min' if students[i] != 2 else '?'
        ax.text(i, t + 1, label, ha='center', fontsize=11, fontweight='bold',
                color=ORANGE if students[i]==2 else 'black')
    save(fig, f'{GFORM_DIR}/q3_car_wash.png')

# GF Q4: Graph of y = 1/(x+5) - 4 with asymptote question
def gform_q4():
    fig, ax = plt.subplots(figsize=(6, 5))
    x1 = np.linspace(-4.8, 10, 300)
    x2 = np.linspace(-15, -5.2, 300)
    y1 = 1/(x1+5) - 4
    y2 = 1/(x2+5) - 4
    ax.plot(x1, y1, color=PURPLE, lw=2.5)
    ax.plot(x2, y2, color=PURPLE, lw=2.5)
    ax.axhline(-4, color=RED, ls='--', lw=2.5)
    ax.axvline(-5, color=BLUE, ls='--', lw=1.5, alpha=0.5)
    ax.annotate('horizontal\nasymptote = ?', xy=(6, -4), fontsize=13,
                color=RED, fontweight='bold',
                xytext=(4, -1.5), arrowprops=dict(arrowstyle='->', color=RED, lw=1.5))
    ax.set_xlim(-12, 12)
    ax.set_ylim(-10, 4)
    ax.set_xlabel('x', fontsize=13)
    ax.set_ylabel('y', fontsize=13)
    ax.set_title(r'$y = \frac{1}{x+5} - 4$', fontsize=20)
    ax.grid(True, alpha=0.3)
    save(fig, f'{GFORM_DIR}/q4_asymptote.png')

# GF Q5: Translation diagram — y=1/x shifted left 2, up 3
def gform_q5():
    fig, ax = plt.subplots(figsize=(6, 5))
    # Parent
    x_pos = np.linspace(0.15, 7, 200)
    x_neg = np.linspace(-7, -0.15, 200)
    ax.plot(x_pos, 1/x_pos, color=GRAY, lw=1.5, ls=':', label=r'$y = \frac{1}{x}$ (parent)')
    ax.plot(x_neg, 1/x_neg, color=GRAY, lw=1.5, ls=':')
    # Translated
    x1 = np.linspace(-1.85, 7, 200)
    x2 = np.linspace(-7, -2.15, 200)
    y1 = 1/(x1+2) + 3
    y2 = 1/(x2+2) + 3
    ax.plot(x1, y1, color=PURPLE, lw=2.5, label=r'translated: $y = ?$')
    ax.plot(x2, y2, color=PURPLE, lw=2.5)
    ax.axhline(3, color=RED, ls='--', lw=1.5, alpha=0.6)
    ax.axvline(-2, color=BLUE, ls='--', lw=1.5, alpha=0.6)
    # Arrows showing shift
    ax.annotate('', xy=(-2, 5), xytext=(0, 5),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=2.5))
    ax.text(-1, 5.4, '← 2 left', fontsize=11, color=GREEN, ha='center', fontweight='bold')
    ax.annotate('', xy=(3, 3), xytext=(3, 0),
                arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2.5))
    ax.text(3.8, 1.5, '↑ 3 up', fontsize=11, color=ORANGE, fontweight='bold')
    ax.set_xlim(-7, 7)
    ax.set_ylim(-4, 10)
    ax.set_xlabel('x', fontsize=13)
    ax.set_ylabel('y', fontsize=13)
    ax.set_title(r'$y = \frac{1}{x}$ translated 3 up and 2 left = ?', fontsize=14)
    ax.legend(fontsize=10, loc='upper right')
    ax.grid(True, alpha=0.3)
    save(fig, f'{GFORM_DIR}/q5_translation.png')


if __name__ == '__main__':
    os.chdir('C:/Users/ColsonR/algebra2')
    os.makedirs(BLOOKET_DIR, exist_ok=True)
    os.makedirs(GFORM_DIR, exist_ok=True)

    print('Generating Blooket graphics...')
    blooket_q1()
    blooket_q2()
    blooket_q3()
    blooket_q4()
    blooket_q5()
    blooket_q6()
    blooket_q7()
    blooket_q8()
    blooket_q9()
    blooket_q10()
    blooket_q11()
    blooket_q12()

    print('\nGenerating Google Form graphics...')
    gform_q1()
    gform_q2()
    gform_q3()
    gform_q4()
    gform_q5()

    print('\nDone! 17 images generated.')
