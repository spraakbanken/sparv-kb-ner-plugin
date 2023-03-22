# Comparison between KBNER and SWENER

Example text: [Ikea example](./texts/ikea-example.xml)

All annotations are runned with `sparv run`.

Running times | mean | values | comment
| - | - | - | -
KBNER | 23.7s | 30s, 25s, 22s, 16s | from xml
SWENER | 66s | 66s | from xml
KBNER | 21s | 21s | from txt
SWENER | 54s | 54s | from txt


```diff
4,6c4
<     <ne ex="ENAMEX" subtype="CRP" type="ORG">
<       <token word="Ikea" pos="PM">Ikea</token>
<     </ne>
---
>     <token word="Ikea" ne_score="0.9993444" ne_type="ORG" pos="PM">Ikea</token>
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
>     <token word="Ingvar" ne_score="0.9993979" ne_type="PRS" pos="PM">Ingvar</token>
>     <token word="Kamprad" ne_score="0.99831116" ne_type="PRS" pos="PM">Kamprad</token>
>     <token word="Elmtaryd" ne_score="0.7953129" ne_type="PRS" pos="PM">Elmtaryd</token>
>     <token word="Agunnaryd" ne_score="0.9898454" ne_type="LOC" pos="PM">Agunnaryd</token>
29,31c23
<     <ne ex="TIMEX" subtype="DAT" type="TME">
<       <token word="1943" pos="RG">1943</token>
<     </ne>
---
>     <token word="1943" ne_score="0.9958897" ne_type="TME" pos="RG">1943</token>
33,36c25,26
<     <ne ex="ENAMEX" subtype="HUM" type="PRS">
<       <token word="Ingvar" pos="PM">Ingvar</token>
<       <token word="Kamprad" pos="PM">Kamprad</token>
<     </ne>
---
>     <token word="Ingvar" ne_score="0.99676883" ne_type="PRS" pos="PM">Ingvar</token>
>     <token word="Kamprad" ne_score="0.9973974" ne_type="PRS" pos="PM">Kamprad</token>
46,48c36
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Nederländerna" pos="PM">Nederländerna</token>
<     </ne>
---
>     <token word="Nederländerna" ne_score="0.9853579" ne_type="LOC" pos="PM">Nederländerna</token>
56,62c44,46
<     <ne ex="ENAMEX" subtype="CRP" type="ORG">
<       <token word="Interogo" pos="PM">Interogo</token>
<     </ne>
<     <token word="i" pos="PP">i</token>
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Luxemburg" pos="PM">Luxemburg</token>
<     </ne>
---
>     <token word="Interogo" ne_score="0.99615014" ne_type="ORG" pos="PM">Interogo</token>
>     <token word="i" pos="PP">i</token>
>     <token word="Luxemburg" ne_score="0.7273218" ne_type="LOC" pos="PM">Luxemburg</token>
69,71c53
<     <ne ex="ENAMEX" subtype="HUM" type="PRS">
<       <token word="Kamprad" pos="PM">Kamprad</token>
<     </ne>
---
>     <token word="Kamprad" ne_score="0.9942551" ne_type="PRS" pos="PM">Kamprad</token>
76,79c58,59
<     <ne ex="TIMEX" subtype="DAT" type="TME">
<       <token word="verksamhetsåret" pos="NN">verksamhetsåret</token>
<       <token word="2012" pos="RG">2012</token>
<     </ne>
---
>     <token word="verksamhetsåret" ne_score="0.9601936" ne_type="TME" pos="NN">verksamhetsåret</token>
>     <token word="2012" ne_score="0.99914443" ne_type="TME" pos="RG">2012</token>
81,86c61,64
<     <token word="Ikeakoncernen" pos="NN">Ikeakoncernen</token>
<     <ne ex="NUMEX" subtype="CUR" type="MSR">
<       <token word="241" pos="RG">241</token>
<       <token word="miljarder" pos="NN">miljarder</token>
<       <token word="kronor" pos="NN">kronor</token>
<     </ne>
---
>     <token word="Ikeakoncernen" ne_score="0.99542964" ne_type="ORG" pos="NN">Ikeakoncernen</token>
>     <token word="241" ne_score="0.99984705" ne_type="MSR" pos="RG">241</token>
>     <token word="miljarder" ne_score="0.9998272" ne_type="MSR" pos="NN">miljarder</token>
>     <token word="kronor" ne_score="0.99974865" ne_type="MSR" pos="NN">kronor</token>
105,107c83
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Sverige" pos="PM">Sverige</token>
<     </ne>
---
>     <token word="Sverige" ne_score="0.9987644" ne_type="LOC" pos="PM">Sverige</token>
110,112c86
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Helsingborg" pos="PM">Helsingborg</token>
<     </ne>
---
>     <token word="Helsingborg" ne_score="0.99904126" ne_type="LOC" pos="PM">Helsingborg</token>
117,119c91
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Helsingborg" pos="PM">Helsingborg</token>
<     </ne>
---
>     <token word="Helsingborg" ne_score="0.9992242" ne_type="LOC" pos="PM">Helsingborg</token>
121,123c93
<     <ne ex="TIMEX" subtype="DAT" type="TME">
<       <token word="idag" pos="AB">idag</token>
<     </ne>
---
>     <token word="idag" ne_score="0.99955255" ne_type="TME" pos="AB">idag</token>
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
>     <token word="Malmö" ne_score="0.9993656" ne_type="LOC" pos="PM">Malmö</token>
>     <token word="1" ne_score="0.99970883" ne_type="TME" pos="RO">1</token>
>     <token word="september" ne_score="0.9997042" ne_type="TME" pos="NN">september</token>
>     <token word="2015" ne_score="0.9995536" ne_type="TME" pos="RG">2015</token>
172,173c138,139
<     <token word="Vintrie" pos="PM">Vintrie</token>
<     <token word="park" pos="NN">park</token>
---
>     <token word="Vintrie" ne_score="0.99885845" ne_type="LOC" pos="PM">Vintrie</token>
>     <token word="park" ne_score="0.9985474" ne_type="LOC" pos="NN">park</token>
177,179c143
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Svågertorp" pos="PM">Svågertorp</token>
<     </ne>
---
>     <token word="Svågertorp" ne_score="0.9993649" ne_type="LOC" pos="PM">Svågertorp</token>
208,210c172
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Mellanöstern" pos="PM">Mellanöstern</token>
<     </ne>
---
>     <token word="Mellanöstern" ne_score="0.9992446" ne_type="LOC" pos="PM">Mellanöstern</token>
212,213c174,175
<     <token word="spanska" pos="JJ">spanska</token>
<     <token word="öarna" pos="NN">öarna</token>
---
>     <token word="spanska" ne_score="0.9756647" ne_type="LOC" pos="JJ">spanska</token>
>     <token word="öarna" ne_score="0.94374675" ne_type="LOC" pos="NN">öarna</token>
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
>     <token word="Tyskland" ne_score="0.9994412" ne_type="LOC" pos="PM">Tyskland</token>
>     <token word="16" ne_score="0.9997459" ne_type="MSR" pos="RG">16</token>
>     <token word="%" ne_score="0.9997576" ne_type="MSR" pos="NN">%</token>
>     <token word="," pos="MID">,</token>
>     <token word="USA" ne_score="0.9989587" ne_type="LOC" pos="PM">USA</token>
>     <token word="11" ne_score="0.99974734" ne_type="MSR" pos="RG">11</token>
>     <token word="%" ne_score="0.9997259" ne_type="MSR" pos="NN">%</token>
>     <token word="," pos="MID">,</token>
>     <token word="Frankrike" ne_score="0.9993937" ne_type="LOC" pos="PM">Frankrike</token>
>     <token word="10" ne_score="0.9997701" ne_type="MSR" pos="RG">10</token>
>     <token word="%" ne_score="0.99973327" ne_type="MSR" pos="NN">%</token>
>     <token word="," pos="MID">,</token>
>     <token word="Storbritannien" ne_score="0.9995326" ne_type="LOC" pos="PM">Storbritannien</token>
>     <token word="7" ne_score="0.99969697" ne_type="MSR" pos="RG">7</token>
>     <token word="%" ne_score="0.9996772" ne_type="MSR" pos="NN">%</token>
261,267c207,209
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Italien" pos="PM">Italien</token>
<     </ne>
<     <ne ex="NUMEX" subtype="PRC" type="MSR">
<       <token word="7" pos="RG">7</token>
<       <token word="%" pos="NN">%</token>
<     </ne>
---
>     <token word="Italien" ne_score="0.99951017" ne_type="LOC" pos="PM">Italien</token>
>     <token word="7" ne_score="0.9996611" ne_type="MSR" pos="RG">7</token>
>     <token word="%" ne_score="0.99962115" ne_type="MSR" pos="NN">%</token>
272,274c214
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Sverige" pos="PM">Sverige</token>
<     </ne>
---
>     <token word="Sverige" ne_score="0.99893314" ne_type="LOC" pos="PM">Sverige</token>
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
>     <token word="Borlänge" ne_score="0.9987342" ne_type="LOC" pos="PM">Borlänge</token>
>     <token word="25" ne_score="0.99964535" ne_type="TME" pos="RG">25</token>
>     <token word="oktober" ne_score="0.99968624" ne_type="TME" pos="NN">oktober</token>
>     <token word="2013" ne_score="0.99944836" ne_type="TME" pos="RG">2013</token>
300,302c236
<     <ne ex="TIMEX" subtype="DAT" type="TME">
<       <token word="dessförinnan" pos="AB">dessförinnan</token>
<     </ne>
---
>     <token word="dessförinnan" ne_score="0.9970651" ne_type="TME" pos="AB">dessförinnan</token>
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
>     <token word="Uddevalla" ne_score="0.99919575" ne_type="LOC" pos="PM">Uddevalla</token>
>     <token word="den" ne_score="0.9996189" ne_type="TME" pos="DT">den</token>
>     <token word="8" ne_score="0.9995555" ne_type="TME" pos="RO">8</token>
>     <token word="maj" ne_score="0.9995957" ne_type="TME" pos="NN">maj</token>
>     <token word="2013" ne_score="0.9995789" ne_type="TME" pos="RG">2013</token>
317,322c247,250
<     <ne ex="NUMEX" subtype="MSU" type="MSR">
<       <token word="på" pos="PP">på</token>
<       <token word="37" pos="RG">37</token>
<       <token word="400" pos="RG">400</token>
<       <token word="kvadratmeter" pos="NN">kvadratmeter</token>
<     </ne>
---
>     <token word="på" pos="PP">på</token>
>     <token word="37" ne_score="0.9998572" ne_type="MSR" pos="RG">37</token>
>     <token word="400" ne_score="0.99982446" ne_type="MSR" pos="RG">400</token>
>     <token word="kvadratmeter" ne_score="0.99982625" ne_type="MSR" pos="NN">kvadratmeter</token>
328,330c256
<     <ne ex="ENAMEX" subtype="GPL" type="LOC">
<       <token word="Ikea" pos="PM">Ikea</token>
<     </ne>
---
>     <token word="Ikea" ne_score="0.9797401" ne_type="ORG" pos="PM">Ikea</token>
333,339c259,261
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Haparanda" pos="PM">Haparanda</token>
<     </ne>
<     <token word="i" pos="PP">i</token>
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Sverige" pos="PM">Sverige</token>
<     </ne>
---
>     <token word="Haparanda" ne_score="0.99969614" ne_type="LOC" pos="PM">Haparanda</token>
>     <token word="i" pos="PP">i</token>
>     <token word="Sverige" ne_score="0.99946946" ne_type="LOC" pos="PM">Sverige</token>
344,346c266
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Finland" pos="PM">Finland</token>
<     </ne>
---
>     <token word="Finland" ne_score="0.999281" ne_type="LOC" pos="PM">Finland</token>
348c268
<     <token word="HaparandaTornio" pos="PM">HaparandaTornio</token>
---
>     <token word="HaparandaTornio" ne_score="0.9969266" ne_type="LOC" pos="PM">HaparandaTornio</token>
353,355c273
<     <ne ex="ENAMEX" subtype="CRP" type="ORG">
<       <token word="Ikea" pos="PM">Ikea</token>
<     </ne>
---
>     <token word="Ikea" ne_score="0.9968267" ne_type="ORG" pos="PM">Ikea</token>
358,360c276
<     <ne ex="ENAMEX" subtype="GPL" type="LOC">
<       <token word="Moskva" pos="PM">Moskva</token>
<     </ne>
---
>     <token word="Moskva" ne_score="0.9995691" ne_type="LOC" pos="PM">Moskva</token>
362,365c278,279
<     <ne ex="TIMEX" subtype="DAT" type="TME">
<       <token word="år" pos="NN">år</token>
<       <token word="2005" pos="RG">2005</token>
<     </ne>
---
>     <token word="år" ne_score="0.9996815" ne_type="TME" pos="NN">år</token>
>     <token word="2005" ne_score="0.9996861" ne_type="TME" pos="RG">2005</token>
378,380c292
<     <ne ex="TIMEX" subtype="DAT" type="TME">
<       <token word="Samtidigt" pos="AB">Samtidigt</token>
<     </ne>
---
>     <token word="Samtidigt" ne_score="0.9997255" ne_type="TME" pos="AB">Samtidigt</token>
382,384c294
<     <ne ex="ENAMEX" subtype="CRP" type="ORG">
<       <token word="Ikea" pos="PM">Ikea</token>
<     </ne>
---
>     <token word="Ikea" ne_score="0.9987037" ne_type="ORG" pos="PM">Ikea</token>
387,389c297
<     <ne ex="ENAMEX" subtype="GPL" type="LOC">
<       <token word="Moskva" pos="PM">Moskva</token>
<     </ne>
---
>     <token word="Moskva" ne_score="0.99963665" ne_type="LOC" pos="PM">Moskva</token>
396,397c304,305
<     <token word="Sjeremetievo" pos="PM">Sjeremetievo</token>
<     <token word="internationella" pos="JJ">internationella</token>
---
>     <token word="Sjeremetievo" ne_score="0.9911123" ne_type="LOC" pos="PM">Sjeremetievo</token>
>     <token word="internationella" ne_score="0.61368644" ne_type="LOC" pos="JJ">internationella</token>
408,410c316
<     <ne ex="ENAMEX" subtype="CRP" type="ORG">
<       <token word="Ikea" pos="PM">Ikea</token>
<     </ne>
---
>     <token word="Ikea" ne_score="0.999311" ne_type="ORG" pos="PM">Ikea</token>
453c359
<     <token word="Ikeas" pos="PM">Ikeas</token>
---
>     <token word="Ikeas" ne_score="0.99750453" ne_type="ORG" pos="PM">Ikeas</token>
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
>     <token word="varje" ne_score="0.9994221" ne_type="TME" pos="DT">varje</token>
>     <token word="år" ne_score="0.9990212" ne_type="TME" pos="NN">år</token>
>     <token word="i" ne_score="0.9996105" ne_type="TME" pos="PP">i</token>
>     <token word="augusti" ne_score="0.99937123" ne_type="TME" pos="NN">augusti</token>
```
