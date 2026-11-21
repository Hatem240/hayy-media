# Quranpedia's «تفسير الشعراوي» (book 27803) → spa5k's shape, one file a sura: [{surah, ayah, text}].
# The words stay as they are: only the web page's markup is turned into line breaks; the publisher's footnotes are
# kept, wrapped in [[…]] as Ibn Kathir's editor's notes are (the app leaves those out when it shows the text).
import gzip, json, re, sys, html, os, collections
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
src, out = sys.argv[1], sys.argv[2]
N = [7,286,200,176,120,165,206,75,129,109,123,111,43,52,99,128,111,110,98,135,112,78,118,64,77,227,93,88,69,60,34,30,73,54,45,83,182,88,75,85,54,53,89,59,37,35,38,29,18,45,60,49,62,55,78,96,29,22,24,13,14,11,11,18,12,12,30,52,52,44,28,28,20,56,40,31,50,40,46,42,29,19,36,25,22,17,19,26,30,20,15,21,11,8,8,19,5,8,8,11,11,8,3,9,5,4,7,3,6,3,5,4,5,6]

def plain(t):
    t = t.replace('\r', '')
    # the footnotes' bodies: kept as the editor's notes
    t = re.sub(r'<div class="foot-notes">(.*?)</div>', lambda m: '[[' + re.sub(r'<[^>]+>', ' ', m.group(1)) + ']]', t, flags=re.S)
    t = re.sub(r'<a class="foot-note[^"]*"[^>]*>\s*\(([^)<]*)\)\s*</a>', '', t)  # the marks pointing to them
    t = re.sub(r'</td>\s*<td>', '    ', t)
    t = re.sub(r'<(br|hr|p|/p|tr|/tr|table|/table|h\d|/h\d|h[٠-٩]|/h[٠-٩])\b[^>]*>', '\n', t, flags=re.I)
    t = re.sub(r'<[^>]+>', '', t)
    t = html.unescape(t).replace(' ', ' ')
    t = re.sub(r'[ \t]*\n[ \t\n]*', '\n\n', t)
    t = re.sub(r'[ \t]{2,}', lambda m: m.group(0) if len(m.group(0)) >= 4 else ' ', t)
    return t.strip()

a = json.load(gzip.open(src, 'rt', encoding='utf-8'))['ayahs']
by = collections.defaultdict(dict)
for r in a:
    by[r['surah']][r['ayah']] = '\n\n'.join(plain(c['text']) for c in r['content'])
os.makedirs(out, exist_ok=True)
total = 0
for s in sorted(by):
    rows = [{'surah': s, 'ayah': y, 'text': by[s].get(y, '')} for y in range(1, N[s - 1] + 1)]
    total += sum(1 for r in rows if r['text'])
    with open(f'{out}/{s}.json', 'w', encoding='utf-8', newline='\n') as f:
        json.dump(rows, f, ensure_ascii=False)
print('suras', len(by), 'ayat with text', total)
left = collections.Counter()
for s in by:
    for y, t in by[s].items():
        for m in re.findall(r'<|>|&[a-z#0-9]+;', t): left[m] += 1
print('markup left', left.most_common(5))
