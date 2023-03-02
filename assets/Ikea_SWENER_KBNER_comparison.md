# Comparison between KBNER and SWENER

Example text: [Ikea example](./texts/ikea-example.txt)

All annotations are runned with `sparv run`.

Runtime for KBNER:
- 21s (as txt)
- 30s (as xml)

Runtime for SWENER:
- 54s (as txt)
- 1m6s (as xml)

```diff
4,6c4
<     <ne ex="ENAMEX" subtype="CRP" type="ORG">
<       <token word="Ikea" pos="PM">Ikea</token>
<     </ne>
---
>     <token word="Ikea" kb-ne="ORG" pos="PM">Ikea</token>
14,21c12,15
<     <ne ex="ENAMEX" subtype="HUM" type="PRS">
<       <token word="Ingvar" pos="PM">Ingvar</token>
<       <token word="Kamprad" pos="PM">Kamprad</token>
<       <token word="Elmtaryd" pos="PM">Elmtaryd</token>
<     </ne>
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Agunnaryd" pos="PM">Agunnaryd</token>
<     </ne>
---
>     <token word="Ingvar" kb-ne="PER" pos="PM">Ingvar</token>
>     <token word="Kamprad" kb-ne="PER" pos="PM">Kamprad</token>
>     <token word="Elmtaryd" kb-ne="PER" pos="PM">Elmtaryd</token>
>     <token word="Agunnaryd" kb-ne="LOC" pos="PM">Agunnaryd</token>
29,31c23
<     <ne ex="TIMEX" subtype="DAT" type="TME">
<       <token word="1943" pos="RG">1943</token>
<     </ne>
---
>     <token word="1943" kb-ne="TME" pos="RG">1943</token>
33,36c25,26
<     <ne ex="ENAMEX" subtype="HUM" type="PRS">
<       <token word="Ingvar" pos="PM">Ingvar</token>
<       <token word="Kamprad" pos="PM">Kamprad</token>
<     </ne>
---
>     <token word="Ingvar" kb-ne="PER" pos="PM">Ingvar</token>
>     <token word="Kamprad" kb-ne="PER" pos="PM">Kamprad</token>
46,48c36
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Nederländerna" pos="PM">Nederländerna</token>
<     </ne>
---
>     <token word="Nederländerna" kb-ne="LOC" pos="PM">Nederländerna</token>
56,62c44,46
<     <ne ex="ENAMEX" subtype="CRP" type="ORG">
<       <token word="Interogo" pos="PM">Interogo</token>
<     </ne>
<     <token word="i" pos="PP">i</token>
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Luxemburg" pos="PM">Luxemburg</token>
<     </ne>
---
>     <token word="Interogo" kb-ne="ORG" pos="PM">Interogo</token>
>     <token word="i" pos="PP">i</token>
>     <token word="Luxemburg" kb-ne="LOC" pos="PM">Luxemburg</token>
69,71c53
<     <ne ex="ENAMEX" subtype="HUM" type="PRS">
<       <token word="Kamprad" pos="PM">Kamprad</token>
<     </ne>
---
>     <token word="Kamprad" kb-ne="PER" pos="PM">Kamprad</token>
76,79c58,59
<     <ne ex="TIMEX" subtype="DAT" type="TME">
<       <token word="verksamhetsåret" pos="NN">verksamhetsåret</token>
<       <token word="2012" pos="RG">2012</token>
<     </ne>
---
>     <token word="verksamhetsåret" kb-ne="TME" pos="NN">verksamhetsåret</token>
>     <token word="2012" kb-ne="TME" pos="RG">2012</token>
81,86c61,64
<     <token word="Ikeakoncernen" pos="NN">Ikeakoncernen</token>
<     <ne ex="NUMEX" subtype="CUR" type="MSR">
<       <token word="241" pos="RG">241</token>
<       <token word="miljarder" pos="NN">miljarder</token>
<       <token word="kronor" pos="NN">kronor</token>
<     </ne>
---
>     <token word="Ikeakoncernen" kb-ne="ORG" pos="NN">Ikeakoncernen</token>
>     <token word="241" kb-ne="MSR" pos="RG">241</token>
>     <token word="miljarder" kb-ne="MSR" pos="NN">miljarder</token>
>     <token word="kronor" kb-ne="MSR" pos="NN">kronor</token>
105,107c83
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Sverige" pos="PM">Sverige</token>
<     </ne>
---
>     <token word="Sverige" kb-ne="LOC" pos="PM">Sverige</token>
110,112c86
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Helsingborg" pos="PM">Helsingborg</token>
<     </ne>
---
>     <token word="Helsingborg" kb-ne="LOC" pos="PM">Helsingborg</token>
117,119c91
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Helsingborg" pos="PM">Helsingborg</token>
<     </ne>
---
>     <token word="Helsingborg" kb-ne="LOC" pos="PM">Helsingborg</token>
121,123c93
<     <ne ex="TIMEX" subtype="DAT" type="TME">
<       <token word="idag" pos="AB">idag</token>
<     </ne>
---
>     <token word="idag" kb-ne="TME" pos="AB">idag</token>
151,158c121,124
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Malmö" pos="PM">Malmö</token>
<     </ne>
<     <ne ex="TIMEX" subtype="DAT" type="TME">
<       <token word="1" pos="RO">1</token>
<       <token word="september" pos="NN">september</token>
<       <token word="2015" pos="RG">2015</token>
<     </ne>
---
>     <token word="Malmö" kb-ne="LOC" pos="PM">Malmö</token>
>     <token word="1" kb-ne="TME" pos="RO">1</token>
>     <token word="september" kb-ne="TME" pos="NN">september</token>
>     <token word="2015" kb-ne="TME" pos="RG">2015</token>
172,173c138,139
<     <token word="Vintrie" pos="PM">Vintrie</token>
<     <token word="park" pos="NN">park</token>
---
>     <token word="Vintrie" kb-ne="LOC" pos="PM">Vintrie</token>
>     <token word="park" kb-ne="LOC" pos="NN">park</token>
177,179c143
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Svågertorp" pos="PM">Svågertorp</token>
<     </ne>
---
>     <token word="Svågertorp" kb-ne="LOC" pos="PM">Svågertorp</token>
208,210c172
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Mellanöstern" pos="PM">Mellanöstern</token>
<     </ne>
---
>     <token word="Mellanöstern" kb-ne="LOC" pos="PM">Mellanöstern</token>
212,213c174,175
<     <token word="spanska" pos="JJ">spanska</token>
<     <token word="öarna" pos="NN">öarna</token>
---
>     <token word="spanska" kb-ne="LOC" pos="JJ">spanska</token>
>     <token word="öarna" kb-ne="LOC" pos="NN">öarna</token>
229,259c191,205
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Tyskland" pos="PM">Tyskland</token>
<     </ne>
<     <ne ex="NUMEX" subtype="PRC" type="MSR">
<       <token word="16" pos="RG">16</token>
<       <token word="%" pos="NN">%</token>
<     </ne>
<     <token word="," pos="MID">,</token>
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="USA" pos="PM">USA</token>
<     </ne>
<     <ne ex="NUMEX" subtype="PRC" type="MSR">
<       <token word="11" pos="RG">11</token>
<       <token word="%" pos="NN">%</token>
<     </ne>
<     <token word="," pos="MID">,</token>
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Frankrike" pos="PM">Frankrike</token>
<     </ne>
<     <ne ex="NUMEX" subtype="PRC" type="MSR">
<       <token word="10" pos="RG">10</token>
<       <token word="%" pos="NN">%</token>
<     </ne>
<     <token word="," pos="MID">,</token>
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Storbritannien" pos="PM">Storbritannien</token>
<     </ne>
<     <ne ex="NUMEX" subtype="PRC" type="MSR">
<       <token word="7" pos="RG">7</token>
<       <token word="%" pos="NN">%</token>
<     </ne>
---
>     <token word="Tyskland" kb-ne="LOC" pos="PM">Tyskland</token>
>     <token word="16" kb-ne="MSR" pos="RG">16</token>
>     <token word="%" kb-ne="MSR" pos="NN">%</token>
>     <token word="," pos="MID">,</token>
>     <token word="USA" kb-ne="LOC" pos="PM">USA</token>
>     <token word="11" kb-ne="MSR" pos="RG">11</token>
>     <token word="%" kb-ne="MSR" pos="NN">%</token>
>     <token word="," pos="MID">,</token>
>     <token word="Frankrike" kb-ne="LOC" pos="PM">Frankrike</token>
>     <token word="10" kb-ne="MSR" pos="RG">10</token>
>     <token word="%" kb-ne="MSR" pos="NN">%</token>
>     <token word="," pos="MID">,</token>
>     <token word="Storbritannien" kb-ne="LOC" pos="PM">Storbritannien</token>
>     <token word="7" kb-ne="MSR" pos="RG">7</token>
>     <token word="%" kb-ne="MSR" pos="NN">%</token>
261,267c207,209
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Italien" pos="PM">Italien</token>
<     </ne>
<     <ne ex="NUMEX" subtype="PRC" type="MSR">
<       <token word="7" pos="RG">7</token>
<       <token word="%" pos="NN">%</token>
<     </ne>
---
>     <token word="Italien" kb-ne="LOC" pos="PM">Italien</token>
>     <token word="7" kb-ne="MSR" pos="RG">7</token>
>     <token word="%" kb-ne="MSR" pos="NN">%</token>
272,274c214
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Sverige" pos="PM">Sverige</token>
<     </ne>
---
>     <token word="Sverige" kb-ne="LOC" pos="PM">Sverige</token>
286,293c226,229
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Borlänge" pos="PM">Borlänge</token>
<     </ne>
<     <ne ex="TIMEX" subtype="DAT" type="TME">
<       <token word="25" pos="RG">25</token>
<       <token word="oktober" pos="NN">oktober</token>
<       <token word="2013" pos="RG">2013</token>
<     </ne>
---
>     <token word="Borlänge" kb-ne="LOC" pos="PM">Borlänge</token>
>     <token word="25" kb-ne="TME" pos="RG">25</token>
>     <token word="oktober" kb-ne="TME" pos="NN">oktober</token>
>     <token word="2013" kb-ne="TME" pos="RG">2013</token>
300,302c236
<     <ne ex="TIMEX" subtype="DAT" type="TME">
<       <token word="dessförinnan" pos="AB">dessförinnan</token>
<     </ne>
---
>     <token word="dessförinnan" kb-ne="TME" pos="AB">dessförinnan</token>
306,314c240,244
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Uddevalla" pos="PM">Uddevalla</token>
<     </ne>
<     <ne ex="TIMEX" subtype="DAT" type="TME">
<       <token word="den" pos="DT">den</token>
<       <token word="8" pos="RO">8</token>
<       <token word="maj" pos="NN">maj</token>
<       <token word="2013" pos="RG">2013</token>
<     </ne>
---
>     <token word="Uddevalla" kb-ne="LOC" pos="PM">Uddevalla</token>
>     <token word="den" kb-ne="TME" pos="DT">den</token>
>     <token word="8" kb-ne="TME" pos="RO">8</token>
>     <token word="maj" kb-ne="TME" pos="NN">maj</token>
>     <token word="2013" kb-ne="TME" pos="RG">2013</token>
317,322c247,250
<     <ne ex="NUMEX" subtype="MSU" type="MSR">
<       <token word="på" pos="PP">på</token>
<       <token word="37" pos="RG">37</token>
<       <token word="400" pos="RG">400</token>
<       <token word="kvadratmeter" pos="NN">kvadratmeter</token>
<     </ne>
---
>     <token word="på" pos="PP">på</token>
>     <token word="37" kb-ne="MSR" pos="RG">37</token>
>     <token word="400" kb-ne="MSR" pos="RG">400</token>
>     <token word="kvadratmeter" kb-ne="MSR" pos="NN">kvadratmeter</token>
328,330c256
<     <ne ex="ENAMEX" subtype="GPL" type="LOC">
<       <token word="Ikea" pos="PM">Ikea</token>
<     </ne>
---
>     <token word="Ikea" kb-ne="ORG" pos="PM">Ikea</token>
333,339c259,261
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Haparanda" pos="PM">Haparanda</token>
<     </ne>
<     <token word="i" pos="PP">i</token>
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Sverige" pos="PM">Sverige</token>
<     </ne>
---
>     <token word="Haparanda" kb-ne="LOC" pos="PM">Haparanda</token>
>     <token word="i" pos="PP">i</token>
>     <token word="Sverige" kb-ne="LOC" pos="PM">Sverige</token>
344,346c266
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Finland" pos="PM">Finland</token>
<     </ne>
---
>     <token word="Finland" kb-ne="LOC" pos="PM">Finland</token>
348c268
<     <token word="HaparandaTornio" pos="PM">HaparandaTornio</token>
---
>     <token word="HaparandaTornio" kb-ne="LOC" pos="PM">HaparandaTornio</token>
353,355c273
<     <ne ex="ENAMEX" subtype="CRP" type="ORG">
<       <token word="Ikea" pos="PM">Ikea</token>
<     </ne>
---
>     <token word="Ikea" kb-ne="ORG" pos="PM">Ikea</token>
358,360c276
<     <ne ex="ENAMEX" subtype="GPL" type="LOC">
<       <token word="Moskva" pos="PM">Moskva</token>
<     </ne>
---
>     <token word="Moskva" kb-ne="LOC" pos="PM">Moskva</token>
362,365c278,279
<     <ne ex="TIMEX" subtype="DAT" type="TME">
<       <token word="år" pos="NN">år</token>
<       <token word="2005" pos="RG">2005</token>
<     </ne>
---
>     <token word="år" kb-ne="TME" pos="NN">år</token>
>     <token word="2005" kb-ne="TME" pos="RG">2005</token>
378,380c292
<     <ne ex="TIMEX" subtype="DAT" type="TME">
<       <token word="Samtidigt" pos="AB">Samtidigt</token>
<     </ne>
---
>     <token word="Samtidigt" kb-ne="TME" pos="AB">Samtidigt</token>
382,384c294
<     <ne ex="ENAMEX" subtype="CRP" type="ORG">
<       <token word="Ikea" pos="PM">Ikea</token>
<     </ne>
---
>     <token word="Ikea" kb-ne="ORG" pos="PM">Ikea</token>
387,389c297
<     <ne ex="ENAMEX" subtype="GPL" type="LOC">
<       <token word="Moskva" pos="PM">Moskva</token>
<     </ne>
---
>     <token word="Moskva" kb-ne="LOC" pos="PM">Moskva</token>
396,397c304,305
<     <token word="Sjeremetievo" pos="PM">Sjeremetievo</token>
<     <token word="internationella" pos="JJ">internationella</token>
---
>     <token word="Sjeremetievo" kb-ne="LOC" pos="PM">Sjeremetievo</token>
>     <token word="internationella" kb-ne="LOC" pos="JJ">internationella</token>
408,410c316
<     <ne ex="ENAMEX" subtype="CRP" type="ORG">
<       <token word="Ikea" pos="PM">Ikea</token>
<     </ne>
---
>     <token word="Ikea" kb-ne="ORG" pos="PM">Ikea</token>
453c359
<     <token word="Ikeas" pos="PM">Ikeas</token>
---
>     <token word="Ikeas" kb-ne="ORG" pos="PM">Ikeas</token>
506,513c412,415
<     <ne ex="TIMEX" subtype="DAT" type="TME">
<       <token word="varje" pos="DT">varje</token>
<       <token word="år" pos="NN">år</token>
<     </ne>
<     <ne ex="TIMEX" subtype="DAT" type="TME">
<       <token word="i" pos="PP">i</token>
<       <token word="augusti" pos="NN">augusti</token>
<     </ne>
---
>     <token word="varje" kb-ne="TME" pos="DT">varje</token>
>     <token word="år" kb-ne="TME" pos="NN">år</token>
>     <token word="i" kb-ne="TME" pos="PP">i</token>
>     <token word="augusti" kb-ne="TME" pos="NN">augusti</token>
```
