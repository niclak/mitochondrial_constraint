from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM


def draw_mito():
	with open('figure_scripts/figures/FigureED7_mtDNA.svg', 'w') as svg_output:
		svg_output.write('<svg height="700" width="700" xmlns="http://www.w3.org/2000/svg">\n\n')
		svg_output.write('\n<!-- MARKERS -->\n')
		svg_output.write('<path d="M 143.96241209746475 491.5927694880818 A 250 250 0 0 0 145.64111995882013 494.0050282049715 L 350 350 Z" fill="#ffcc00"></path>')
		svg_output.write('<path d="M 401.3007833865874 105.32014871689486 A 250 250 0 0 0 295.73391917001476 105.96067433433294 L 350 350 Z" fill="#ffcc00"></path>')
		svg_output.write('<path d="M 289.183830631476 107.51001351944655 A 250 250 0 0 0 114.81049156070796 265.2303408047185 L 350 350 Z" fill="#984ea3"></path>')
		svg_output.write('<path d="M 145.64111995882013 494.0050282049715 A 250 250 0 1 0 413.84585747868397 108.29003644282355 L 350 350 Z" fill="#377eb8"></path>')
		svg_output.write('<path d="M 112.49499771206115 271.95274579970055 A 250 250 0 0 0 143.96241209746475 491.5927694880818 L 350 350 Z" fill="#377eb8"></path>')
		svg_output.write('<path d="M 413.84585747868397 108.29003644282355 A 250 250 0 0 0 401.3007833865874 105.32014871689486 L 350 350 Z" fill="#ff7f00"></path>')
		svg_output.write('<path d="M 514.5846094526883 161.81948471930983 A 250 250 0 0 0 509.3128955898264 157.33604047776586 L 350 350 Z" fill="#ff7f00"></path>')
		svg_output.write('<path d="M 598.502774649755 377.3197912029556 A 250 250 0 0 0 599.8552214755076 358.50695606107405 L 350 350 Z" fill="#ff7f00"></path>')
		svg_output.write('<path d="M 530.0554222619816 523.4359965925745 A 250 250 0 0 0 534.2752948018896 518.9455999003131 L 350 350 Z" fill="#ff7f00"></path>')
		svg_output.write('<path d="M 500.72429250648383 549.4547258111974 A 250 250 0 0 0 505.8168539919168 545.5021943919344 L 350 350 Z" fill="#ff7f00"></path>')
		svg_output.write('<path d="M 348.62535868394673 599.9962206939381 A 250 250 0 0 0 357.6304825903442 599.8835243377171 L 350 350 Z" fill="#ff7f00"></path>')
		svg_output.write('<path d="M 271.8401732500997 587.4679799097671 A 250 250 0 0 0 284.55151655053237 591.2809483033519 L 350 350 Z" fill="#ff7f00"></path>')
		svg_output.write('<path d="M 145.64111995882013 494.0050282049715 A 250 250 0 0 0 153.74672389454466 504.86978923558945 L 350 350 Z" fill="#ff7f00"></path>')
		svg_output.write('<path d="M 132.97411588361211 474.09579212648663 A 250 250 0 0 0 143.96241209746475 491.5927694880818 L 350 350 Z" fill="#ff7f00"></path>')
		svg_output.write('<path d="M 100.26204480141641 361.44350179054686 A 250 250 0 0 0 101.92842798917295 380.99185635093596 L 350 350 Z" fill="#ff7f00"></path>')
		svg_output.write('<path d="M 114.81049156070796 265.2303408047185 A 250 250 0 0 0 112.43587291051318 272.13289834461443 L 350 350 Z" fill="#ff7f00"></path>')
		svg_output.write('<path d="M 207.29591946270457 144.73055415380227 A 250 250 0 0 0 201.9743578410495 148.5343471868459 L 350 350 Z" fill="#ff7f00"></path>')
		svg_output.write('<path d="M 295.73391917001476 105.96067433433294 A 250 250 0 0 0 289.183830631476 107.51001351944655 L 350 350 Z" fill="#ff7f00"></path>')
		svg_output.write('<path d="M 552.039495725375 497.24144174462634 A 250 250 0 0 0 551.703957560125 497.70075661479626 L 350 350 Z" fill="#377eb8"></path>')
		svg_output.write('<path d="M 377.20199368894333 598.5156967665155 A 250 250 0 0 0 372.9574183056327 598.943682275209 L 350 350 Z" fill="#377eb8"></path>')
		svg_output.write('<path d="M 100.64012627200816 367.87885271375006 A 250 250 0 0 0 100.62663819279092 367.689726424419 L 350 350 Z" fill="#377eb8"></path>')
		svg_output.write('<circle cx="350" cy="350" r="250" stroke="black" stroke-width="1" fill="transparent"></circle>')
		svg_output.write('<circle cx="350" cy="350" r="240" stroke="none" fill="#ffffff90" filter="url(#blurMe)"></circle>')
		svg_output.write('<circle cx="350" cy="350" r="225" stroke="none" fill="#ffffffd0" filter="url(#blurMe)"></circle>')
		svg_output.write('<circle cx="350" cy="350" r="220" stroke="black" stroke-width="1" fill="white"></circle>')
		svg_output.write('<line x1="295.73391917001476" y1="105.96067433433294" x2="302.245848869613" y2="135.24539341421297" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="289.183830631476" y1="107.51001351944655" x2="296.48177095569883" y2="136.60881189711296" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="207.29591946270457" y1="144.73055415380227" x2="224.42040912718005" y2="169.36288765534601" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="201.9743578410495" y1="148.5343471868459" x2="219.7374349001236" y2="172.7102255244244" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="114.81049156070796" y1="265.2303408047185" x2="143.033232573423" y2="275.4026999081523" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="112.49499771206118" y1="271.9527457997005" x2="140.99559798661383" y2="281.3184163037364" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="112.43587291051318" y1="272.13289834461443" x2="140.9435681612516" y2="281.47695054326067" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="100.26204480141641" y1="361.44350179054686" x2="130.23059942524642" y2="360.07028157568124" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="100.64012627200816" y1="367.87885271375006" x2="130.56331111936717" y2="365.7333903881" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="100.62663819279092" y1="367.689726424419" x2="130.551441609656" y2="365.56695925348873" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="101.20251194884742" y1="374.4910175255457" x2="131.05821051498572" y2="371.55209542248025" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="101.21181715728642" y1="374.5853630809169" x2="131.06639909841203" y2="371.6351195112069" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="101.92842798917295" y1="380.99185635093596" x2="131.6970166304722" y2="377.2728335888237" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="132.97411588361211" y1="474.09579212648663" x2="159.01722197757866" y2="459.20429707130825" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="136.24590903385118" y1="479.6502548984589" x2="161.89639994978901" y2="464.0922243106438" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="136.59081743526949" y1="480.21720622503585" x2="162.19991934303715" y2="464.59114147803155" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="140.07070596897375" y1="485.75599989552916" x2="165.2622212526969" y2="469.46527990806567" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="140.12220154380086" y1="485.8355981147028" x2="165.30753735854475" y2="469.53532634093847" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="143.96241209746475" y1="491.5927694880818" x2="168.68692264576896" y2="474.60163714951193" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="145.64111995882013" y1="494.0050282049715" x2="170.1641855637617" y2="476.7244248203749" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="149.25239871024732" y1="498.9979884978669" x2="173.34211086501764" y2="481.1182298781229" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="153.04401406803598" y1="503.97512658078244" x2="176.67873237987166" y2="485.49811139108857" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="153.74672389454457" y1="504.8697892355894" x2="177.29711702719922" y2="486.28541452731866" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="271.8401732500997" y1="587.4679799097671" x2="281.21935246008775" y2="558.971822320595" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="278.0797388618457" y1="589.4315685907347" x2="286.71017019842424" y2="560.6997803598465" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="278.3521722553664" y1="589.5132329944952" x2="286.94991158472243" y2="560.7716450351556" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="284.55151655053237" y1="591.2809483033519" x2="292.4053345644685" y2="562.3272345069497" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="348.6253586839465" y1="599.9962206939381" x2="348.7903156418729" y2="569.9966742106656" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="350.99543230428696" y1="599.9980182212003" x2="350.8759804277725" y2="569.9982560346563" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="357.6304825903442" y1="599.8835243377171" x2="356.7148246795029" y2="569.897501417191" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="357.72524119741416" y1="599.8806127902718" x2="356.79821225372444" y2="569.8949392554392" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="377.2019936889431" y1="598.5156967665155" x2="373.93775444626993" y2="568.6938131545337" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="372.9574183056325" y1="598.9436822752091" x2="370.2025281089566" y2="569.070440402184" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="435.6831831964336" y1="584.8582383424656" x2="425.40120121286157" y2="556.6752497413697" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="500.72429250648383" y1="549.4547258111974" x2="482.63737740570576" y2="525.5201587138537" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="505.8168539919168" y1="545.5021943919344" x2="487.1188315128868" y2="522.0419310649022" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="530.0554222619816" y1="523.4359965925745" x2="508.4487715905438" y2="502.6236770014655" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="534.2752948018896" y1="518.9455999003131" x2="512.1622594256628" y2="498.6721279122755" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="552.039495725375" y1="497.24144174462634" x2="527.7947562383299" y2="479.5724687352712" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="551.7039575601252" y1="497.7007566147961" x2="527.4994826529102" y2="479.97666582102056" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="598.502774649755" y1="377.3197912029556" x2="568.6824416917843" y2="374.041416258601" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="599.1324718293299" y1="370.8089278966546" x2="569.2365752098103" y2="368.311856549056" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="599.5356508783503" y1="365.2301983151254" x2="569.5913727729483" y2="363.4025745173103" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="599.8552214755076" y1="358.5069560610743" x2="569.8725948984467" y2="357.48612133374536" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="548.5509563353202" y1="198.08713767975476" x2="524.7248415750818" y2="216.3166811581842" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="514.5846094526881" y1="161.81948471930968" x2="494.8344563183656" y2="184.40114655299251" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="509.60495515076866" y1="157.57791631072817" x2="490.4523605326764" y2="180.66856635344078" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="509.3128955898262" y1="157.33604047776572" x2="490.1953481190471" y2="180.45571562043384" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="413.84585747868397" y1="108.29003644282355" x2="406.1843545812419" y2="137.29523206968474" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="407.77695749897515" y1="106.76796431768776" x2="400.8437225990981" y2="135.95580859956522" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="407.5924672497638" y1="106.72421469434141" x2="400.6813711797921" y2="135.91730893102044" stroke="black" stroke-width="1"></line>')
		svg_output.write('<line x1="401.3007833865872" y1="105.32014871689483" x2="395.1446893801967" y2="134.68173087086745" stroke="black" stroke-width="1"></line>')
		# svg_output.write('<text x="291.34978611049434" y="101.83644020381391" text-anchor="end" transform="rotate(76.70287887017925,291.34978611049434,101.83644020381391)" fill="black" font-size="10" font-family="arial" alignment-baseline="central" id="MT-TF" class="label">MT-TF</text>')
		# svg_output.write('<text x="244.52717400609274" y="117.8352245131511" text-anchor="end" transform="rotate(65.56762629005975,244.52717400609274,117.8352245131511)" fill="black" font-size="10" font-family="arial" alignment-baseline="central" id="MT-RNR1" class="label">MT-RNR1</text>')
		# svg_output.write('<text x="201.7544883682186" y="142.51923394918902" text-anchor="end" transform="rotate(54.45410103204781,201.7544883682186,142.51923394918902)" fill="black" font-size="10" font-family="arial" alignment-baseline="central" id="MT-TV" class="label">MT-TV</text>')
		# svg_output.write('<text x="145.72838206570614" y="197.3628285557352" text-anchor="end" transform="rotate(36.7680608365019,145.72838206570614,197.3628285557352)" fill="black" font-size="10" font-family="arial" alignment-baseline="central" id="MT-RNR2" class="label">MT-RNR2</text>')
		# svg_output.write('<text x="108.91717237264496" y="266.90926511819134" text-anchor="end" transform="rotate(19.01683867463336,108.91717237264496,266.90926511819134)" fill="black" font-size="10" font-family="arial" alignment-baseline="central" id="MT-TL1" class="label">MT-TL1</text>')
		# svg_output.write('<text x="97.34298993803469" y="315.51180975249696" text-anchor="end" transform="rotate(7.772949483976107,97.34298993803469,315.51180975249696)" fill="black" font-size="10" font-family="arial" alignment-baseline="central" id="MT-ND1" class="label">MT-ND1</text>')
		# svg_output.write('<text x="95.43894894024572" y="364.9556438628761" text-anchor="end" transform="rotate(-3.3623030961434015,95.43894894024572,364.9556438628761)" fill="black" font-size="10" font-family="arial" alignment-baseline="baseline" id="MT-TI" class="label">MT-TI</text>')
		# svg_output.write('<text x="95.90511503331439" y="371.4660064699235" text-anchor="end" transform="rotate(-4.828897338403023,95.90511503331439,371.4660064699235)" fill="black" font-size="10" font-family="arial" alignment-baseline="central" id="MT-TQ" class="label">MT-TQ</text>')
		# svg_output.write('<text x="96.57509142158989" y="378.29868746116114" text-anchor="end" transform="rotate(-6.371537208039122,96.57509142158989,378.29868746116114)" fill="black" font-size="10" font-family="arial" alignment-baseline="hanging" id="MT-TM" class="label">MT-TM</text>')
		# svg_output.write('<text x="108.07907771035795" y="430.6180337054245" text-anchor="end" transform="rotate(-18.43020097772948,108.07907771035795,430.6180337054245)" fill="black" font-size="10" font-family="arial" alignment-baseline="central" id="MT-ND2" class="label">MT-ND2</text>')
		# svg_output.write('<text x="134.05318077436996" y="485.61700212854237" text-anchor="end" transform="rotate(-32.12927756653992,134.05318077436996,485.61700212854237)" fill="black" font-size="10" font-family="arial" alignment-baseline="middle" id="MT-TA" class="label">MT-TA</text>')
		# svg_output.write('<text x="137.83600662430004" y="491.4617966621234" text-anchor="end" transform="rotate(-33.69364475828355,137.83600662430004,491.4617966621234)" fill="black" font-size="10" font-family="arial" alignment-baseline="central" id="MT-TN" class="label">MT-TN</text>')
		# svg_output.write('<text x="143.38000279503697" y="499.44288793723524" text-anchor="end" transform="rotate(-35.877240630092345,143.38000279503697,499.44288793723524)" fill="black" font-size="10" font-family="arial" alignment-baseline="central" id="MT-TC" class="label">MT-TC</text>')
		# svg_output.write('<text x="147.12599189962066" y="504.4899247112485" text-anchor="end" transform="rotate(-37.28951656708312,147.12599189962066,504.4899247112485)" fill="black" font-size="10" font-family="arial" alignment-baseline="hanging" id="MT-TY" class="label">MT-TY</text>')
		# svg_output.write('<text x="203.80732684859717" y="558.9322912257632" text-anchor="end" transform="rotate(-55.01901140684411,203.80732684859717,558.9322912257632)" fill="black" font-size="10" font-family="arial" alignment-baseline="central" id="MT-CO1" class="label">MT-CO1</text>')
		# svg_output.write('<text x="273.4064858305164" y="593.2250677606424" text-anchor="end" transform="rotate(-72.52036936447583,273.4064858305164,593.2250677606424)" fill="black" font-size="10" font-family="arial" alignment-baseline="middle" id="MT-TS1" class="label">MT-TS1</text>')
		# svg_output.write('<text x="280.02857423931806" y="595.2121521805503" text-anchor="end" transform="rotate(-74.07387289516565,280.02857423931806,595.2121521805503)" fill="black" font-size="10" font-family="arial" alignment-baseline="central" id="MT-TD" class="label">MT-TD</text>')
		# svg_output.write('<text x="315.5836693218969" y="602.6668086287858" text-anchor="end" transform="rotate(-82.24334600760456,315.5836693218969,602.6668086287858)" fill="black" font-size="10" font-family="arial" alignment-baseline="central" id="MT-CO2" class="label">MT-CO2</text>')
		# svg_output.write('<text x="354.3512615253089" y="604.9628728327682" text-anchor="start" transform="rotate(-270.97772949483976,354.3512615253089,604.9628728327682)" fill="black" font-size="10" font-family="arial" alignment-baseline="central" id="MT-TK" class="label">MT-TK</text>')
		# svg_output.write('<text x="367.8264861354817" y="604.3761317263502" text-anchor="start" transform="rotate(-274.00869092884307,367.8264861354817,604.3761317263502)" fill="black" font-size="10" font-family="arial" alignment-baseline="central" id="MT-ATP8" class="label">MT-ATP8</text>')
		# svg_output.write('<text x="405.87044768601726" y="598.8041259211029" text-anchor="start" transform="rotate(-282.656165127648,405.87044768601726,598.8041259211029)" fill="black" font-size="10" font-family="arial" alignment-baseline="central" id="MT-ATP6" class="label">MT-ATP6</text>')
		# svg_output.write('<text x="471.869832288125" y="573.9927319759825" text-anchor="start" transform="rotate(-298.549701249321,471.869832288125,573.9927319759825)" fill="black" font-size="10" font-family="arial" alignment-baseline="central" id="MT-CO3" class="label">MT-CO3</text>')
		# svg_output.write('<text x="506.3107818659553" y="551.4744139399685" text-anchor="start" transform="rotate(-307.8055404671374,506.3107818659553,551.4744139399685)" fill="black" font-size="10" font-family="arial" alignment-baseline="central" id="MT-TG" class="label">MT-TG</text>')
		# svg_output.write('<text x="521.6283825620894" y="538.5966550581454" text-anchor="start" transform="rotate(-312.3030961434003,521.6283825620894,538.5966550581454)" fill="black" font-size="10" font-family="arial" alignment-baseline="central" id="MT-ND3" class="label">MT-ND3</text>')
		# svg_output.write('<text x="535.7896640395311" y="524.6631063965087" text-anchor="start" transform="rotate(-316.76806083650195,535.7896640395311,524.6631063965087)" fill="black" font-size="10" font-family="arial" alignment-baseline="central" id="MT-TR" class="label">MT-TR</text>')
		# svg_output.write('<text x="547.3312440105284" y="511.50969053668985" text-anchor="start" transform="rotate(-320.7007061379685,547.3312440105284,511.50969053668985)" fill="black" font-size="10" font-family="arial" alignment-baseline="central" id="MT-ND4L" class="label">MT-ND4L</text>')
		# svg_output.write('<text x="587.6543392003693" y="442.4414141996745" text-anchor="start" transform="rotate(-338.74524714828897,587.6543392003693,442.4414141996745)" fill="black" font-size="10" font-family="arial" alignment-baseline="central" id="MT-ND4" class="label">MT-ND4</text>')
		# svg_output.write('<text x="603.811038115901" y="374.5958722254079" text-anchor="start" transform="rotate(-354.46496469310154,603.811038115901,374.5958722254079)" fill="black" font-size="10" font-family="arial" alignment-baseline="hanging" id="MT-TH" class="label">MT-TH</text>')
		# svg_output.write('<text x="604.3331670585409" y="368.4293280933496" text-anchor="start" transform="rotate(-355.8555133079847,604.3331670585409,368.4293280933496)" fill="black" font-size="10" font-family="arial" alignment-baseline="central" id="MT-TS2" class="label">MT-TS2</text>')
		# svg_output.write('<text x="604.7101248315092" y="362.1553407322448" text-anchor="start" transform="rotate(-357.2677892449756,604.7101248315092,362.1553407322448)" fill="black" font-size="10" font-family="arial" alignment-baseline="baseline" id="MT-TL2" class="label">MT-TL2</text>')
		# svg_output.write('<text x="592.8960960039831" y="272.36955142456105" text-anchor="start" transform="rotate(-377.7240630092341,592.8960960039831,272.36955142456105)" fill="black" font-size="10" font-family="arial" alignment-baseline="central" id="MT-ND5" class="label">MT-ND5</text>')
		# svg_output.write('<text x="536.1535498394038" y="175.72476973996388" text-anchor="start" transform="rotate(-403.11243889190655,536.1535498394038,175.72476973996388)" fill="black" font-size="10" font-family="arial" alignment-baseline="central" id="MT-ND6" class="label">MT-ND6</text>')
		# svg_output.write('<text x="515.3876327873351" y="155.907416625463" text-anchor="start" transform="rotate(-409.565453557849,515.3876327873351,155.907416625463)" fill="black" font-size="10" font-family="arial" alignment-baseline="central" id="MT-TE" class="label">MT-TE</text>')
		# svg_output.write('<text x="466.5702920021593" y="123.20412917662873" text-anchor="start" transform="rotate(-422.7973927213471,466.5702920021593,123.20412917662873)" fill="black" font-size="10" font-family="arial" alignment-baseline="central" id="MT-CYB" class="label">MT-CYB</text>')
		# svg_output.write('<text x="412.07938890987447" y="102.67198000918586" text-anchor="start" transform="rotate(-435.90983161325363,412.07938890987447,102.67198000918586)" fill="black" font-size="10" font-family="arial" alignment-baseline="central" id="MT-TT" class="label">MT-TT</text>')
		# svg_output.write('<text x="405.58736208540654" y="101.13247464487071" text-anchor="start" transform="rotate(-437.4090168386746,405.58736208540654,101.13247464487071)" fill="black" font-size="10" font-family="arial" alignment-baseline="middle" id="MT-TP" class="label">MT-TP</text>')
		svg_output.write('<filter id="blurMe"><feGaussianBlur in="SourceGraphic" stdDeviation="2"></feGaussianBlur></filter>')
		svg_output.write('</svg>')


if __name__ == "__main__":
	draw_mito()
	figure = svg2rlg('figure_scripts/figures/FigureED7_mtDNA.svg')
	renderPM.drawToFile(figure, 'figure_scripts/figures/FigureED8_mtDNA.png', fmt='PNG')