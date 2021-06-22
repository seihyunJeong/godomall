import os

current_dir = os.path.dirname(os.path.realpath(__file__))

products = [
    '1000000022',
    '1000000035',
    '1000000036',
    '1000000045',
    '1000000046',
    '1000000047',
    '1000000048',
    '1000000053',
    '1000000054',
    '1000000055',
    '1000000056',
    '1000000057',
    '1000000058',
    '1000000063',
    '1000000064',
    '1000000068',
    '1000000100',
    '1000000114',
    '1000000116',
    '1000000143',
    '1000000144',
    '1000000148',
    '1000000152',
    '1000000406',
    '1000000411',
    '1000000416',
    '1000000417',
    '1000000418',
    '1000000432',
    '1000000450',
    '1000000456',
    '1000000461',
    '1000000462',
    '1000000497',
    '1000000575',
    '1000000603',
    '1000000630',
    '1000000663',
    '1000000676',
    '1000000707',
    '1000000720',
    '1000000731',
    '1000000732',
    '1000000766',
    '1000000768',
    '1000000777',
    '1000000783',
    '1000000808',
    '1000000809',
    '1000000895',
    '1000000910',
    '1000000911',
    '1000000912',
    '1000000913',
    '1000000914',
    '1000000915',
    '1000000921',
    '1000000922',
    '1000000925',
    '1000000942',
    '1000001000',
    '1000001083',
    '1000001084',
    '1000001085',
    '1000001087',
    '1000001125',
    '1000001128',
    '1000001130',
    '1000001131',
    '1000001140',
    '1000001142',
    '1000001145',
    '1000001146',
    '1000001147',
    '1000001155',
    '1000001168',
    '1000001170',
    '1000001171',
    '1000001174',
    '1000001217',
    '1000001283',
    '1000001314',
    '1000001321',
    '1000001324',
    '1000001325',
    '1000001326',
    '1000001327',
    '1000001328',
    '1000001329',
    '1000001330',
    '1000001342',
    '1000001343',
    '1000001344',
    '1000001347',
    '1000001348',
    '1000001355',
    '1000001365',
    '1000001366',
    '1000001381',
    '1000001447',
    '1000001450',
    '1000001451',
    '1000001459',
    '1000001460',
    '1000001528',
    '1000001531',
    '1000001548',
    '1000001581',
    '1000001597',
    '1000001605',
    '1000001621',
    '1000001626',
    '1000001656',
    '1000001708',
    '1000001709',
    '1000001711',
    '1000001761',
    '1000001779',
    '1000001837',
    '1000001838',
    '1000001839',
    '1000001840',
    '1000001935',
    '1000001936',
    '1000001965',
    '1000001968',
    '1000001969',
    '1000001970',
    '1000001978',
    '1000001979',
    '1000001982',
    '1000001988',
    '1000001996',
    '1000001998',
    '1000001999',
    '1000002000',
    '1000002048',
    '1000002055',
    '1000002056',
    '1000002073',
    '1000002074',
    '1000002075',
    '1000002077',
    '1000002091',
    '1000002093',
    '1000002094',
    '1000002095',
    '1000002097',
    '1000002098',
    '1000002180',
    '1000002184',
    '1000002191',
    '1000002206',
    '1000002208',
    '1000002210',
    '1000002211',
    '1000002214',
    '1000002216',
    '1000002217',
    '1000002220',
    '1000002234',
    '1000002238',
    '1000002254',
    '1000002255',
    '1000002256',
    '1000002257',
    '1000002258',
    '1000002259',
    '1000002262',
    '1000002277',
    '1000002283',
    '1000002290',
    '1000002293',
    '1000002294',
    '1000002295',
    '1000002296',
    '1000002297',
    '1000002298',
    '1000002299',
    '1000002301',
    '1000002328',
    '1000002365',
    '1000002366',
    '1000002367',
    '1000002368',
    '1000002369',
    '1000002374',
    '1000002376',
    '1000002379',
    '1000002380',
    '1000002381',
    '1000002382',
    '1000002383',
    '1000002384',
    '1000002385',
    '1000002387',
    '1000002389',
    '1000002390',
    '1000002391',
    '1000002392',
    '1000002404',
    '1000002406',
    '1000002407',
    '1000002451',
    '1000002465',
    '1000002523',
    '1000002524',
    '1000002526',
    '1000002527',
    '1000002528',
    '1000002529',
    '1000002530',
    '1000002531',
    '1000002532',
    '1000002533',
    '1000002534',
    '1000002536',
    '1000002573',
    '1000002576',
    '1000002578',
    '1000002616',
    '1000002619',
    '1000002620',
    '1000002621',
    '1000002622',
    '1000002623',
    '1000002625',
    '1000002626',
    '1000002627',
    '1000002633',
    '1000002638',
    '1000002643',
    '1000002666',
    '1000002670',
    '1000002671',
    '1000002691',
    '1000002692',
    '1000002696',
    '1000002704',
    '1000002726',
    '1000002727',
    '1000002730',
    '1000002732',
    '1000002736',
    '1000002737',
    '1000002738',
    '1000002761',
    '1000002764',
    '1000002775',
    '1000002776',
    '1000002777',
    '1000002778',
    '1000002780',
    '1000002781',
    '1000002782',
    '1000002789',
    '1000002799',
    '1000002817',
    '1000002823',
    '1000002860',
    '1000002865',
    '1000002879',
    '1000002950',
    '1000002976',
    '1000002990',
    '1000002991',
    '1000003024',
    '1000003033',
    '1000003088',
    '1000003102',
    '1000003140',
    '1000003141',
    '1000003142',
    '1000003151',
    '1000003177',
    '1000003440',
    '1000003470',
    '1000003477',
    '1000003478',
    '1000003489',
    '1000003538',
    '1000003542',
    '1000003569',
    '1000003576',
    '1000003607',
    '1000003611',
    '1000003613',
    '1000003614',
    '1000003619',
    '1000003620',
    '1000003621',
    '1000003625',
    '1000003642',
    '1000003643',
    '1000003668',
    '1000003687',
    '1000003688',
    '1000003694',
    '1000003699',
    '1000003711',
    '1000003813',
    '1000003822',
    '1000003826',
    '1000003829',
    '1000003860',
    '1000003869',
    '1000003870',
    '1000003871',
    '1000003872',
    '1000003873',
    '1000003874',
    '1000003875',
    '1000003878',
    '1000003953',
    '1000003954',
    '1000003955',
    '1000003956',
    '1000003957',
    '1000003959',
    '1000003960',
    '1000003961',
    '1000003962',
    '1000003998',
    '1000004033',
    '1000004068',
    '1000004081',
    '1000004082',
    '1000004085',
    '1000004088',
    '1000004107',
    '1000004133',
    '1000004148',
    '1000004201',
    '1000004203',
    '1000004213',
    '1000004217',
    '1000004270',
    '1000004271',
    '1000004272',
    '1000004342',
    '1000004356',
    '1000004380',
    '1000004381',
    '1000004392',
    '1000004413',
    '1000004415',
    '1000004417',
    '1000004420',
    '1000004421',
    '1000004425',
    '1000004427',
    '1000004428',
    '1000004429',
    '1000004432',
    '1000004443',
    '1000004444',
    '1000004459',
    '1000004466',
    '1000004467',
    '1000004485',
    '1000004501',
    '1000004516',
    '1000004522',
    '1000004533',
    '1000004534',
    '1000004536',
    '1000004548',
    '1000004552',
    '1000004582',
    '1000004593',
    '1000004595',
    '1000004596',
    '1000004606',
    '1000004612',
    '1000004613',
    '1000004616',
    '1000004617',
    '1000004642',
    '1000004643',
    '1000004762',
    '1000004768',
    '1000004783',
    '1000004795',
    '1000004799',
    '1000004805',
    '1000004905',
    '1000004918',
    '1000004919',
    '1000004924',
    '1000004940',
    '1000004946',
    '1000004947',
    '1000004948',
    '1000004961',
    '1000004963',
    '1000004964',
    '1000004973',
    '1000004974',
    '1000004975',
    '1000004976',
    '1000004977',
    '1000004978',
    '1000004979',
    '1000004980',
    '1000004981',
    '1000004982',
    '1000004983',
    '1000004984',
    '1000004985',
    '1000004986',
    '1000004989',
    '1000004992',
    '1000004994',
    '1000004996',
    '1000005005',
    '1000005017',
    '1000005026',
    '1000005027',
    '1000005032',
    '1000005035',
    '1000005117',
    '1000005118',
    '1000005119',
    '1000005120',
    '1000005127',
    '1000005152',
    '1000005158',
    '1000005159',
    '1000005188',
    '1000005250',
    '1000005254',
    '1000005255',
    '1000005256',
    '1000005259',
    '1000005260',
    '1000005392',
    '1000005401',
    '1000005402',
    '1000005408',
    '1000005409',
    '1000005423',
    '1000005424',
    '1000005425',
    '1000005426',
    '1000005427',
    '1000005428',
    '1000005439',
    '1000005443',
    '1000005452',
    '1000005473',
    '1000005478',
    '1000005499',
    '1000005506',
    '1000005508',
    '1000005514',
    '1000005515',
    '1000005516',
    '1000005517',
    '1000005518',
    '1000005519',
    '1000005520',
    '1000005521',
    '1000005522',
    '1000005523',
    '1000005524',
    '1000005525',
    '1000005526',
    '1000005527',
    '1000005528',
    '1000005529',
    '1000005530',
    '1000005555',
    '1000005564',
    '1000005565',
    '1000005579',
    '1000005587',
    '1000005594',
    '1000005596',
    '1000005603',
    '1000005604',
    '1000005618',
    '1000005619',
    '1000005620',
    '1000005627',
    '1000005632',
    '1000005633',
    '1000005634',
    '1000005635',
    '1000005636',
    '1000005637',
    '1000005638',
    '1000005639',
    '1000005640',
    '1000005641',
    '1000005642',
    '1000005643',
    '1000005649',
    '1000005659',
    '1000005664',
    '1000005680',
    '1000005683',
    '1000005685',
    '1000005699',
    '1000005735',
    '1000005744',
    '1000005745',
    '1000005747',
    '1000005750',
    '1000005758',
    '1000005762',
    '1000005773',
    '1000005774',
    '1000005775',
    '1000005777',
    '1000005778',
    '1000005779',
    '1000005780',
    '1000005781',
    '1000005782',
    '1000005783',
    '1000005787',
    '1000005795',
    '1000005796',
    '1000005797',
    '1000005798',
    '1000005799',
    '1000005800',
    '1000005801',
    '1000005803',
    '1000005804',
    '1000005805',
    '1000005807',
    '1000005808',
    '1000005809',
    '1000005810',
    '1000005811',
    '1000005812',
    '1000005813',
    '1000005814',
    '1000005838',
    '1000005839',
    '1000005844',
    '1000005845',
    '1000005846',
    '1000005850',
    '1000005851',
    '1000005852',
    '1000005853',
    '1000005854',
    '1000005856',
    '1000005857',
    '1000005858',
    '1000005861',
    '1000005862',
    '1000005863',
    '1000005864',
    '1000005865',
    '1000005866',
    '1000005867',
    '1000005869',
    '1000005870',
    '1000005871',
    '1000005872',
    '1000005873',
    '1000005874',
    '1000005875',
    '1000005876',
    '1000005877',
    '1000005878',
    '1000005879',
    '1000005880',
    '1000005881',
    '1000005882',
    '1000005883',
    '1000005885',
    '1000005886',
    '1000005887',
    '1000005888',
    '1000005889',
    '1000005890',
    '1000005891',
    '1000005892',
    '1000005893',
    '1000005894',
    '1000005895',
    '1000005896',
    '1000005897',
    '1000005898',
    '1000005899',
    '1000005900',
    '1000005901',
    '1000005902',
    '1000005903',
    '1000005904',
    '1000005905',
    '1000005906',
    '1000005907',
    '1000005908',
    '1000005909',
    '1000005910',
    '1000005911',
    '1000005912',
    '1000005913',
    '1000005914',
    '1000005915',
    '1000005916',
    '1000005917',
    '1000005918',
    '1000005919',
    '1000005920',
    '1000005921',
    '1000005922',
    '1000005923',
    '1000005924',
    '1000005925',
    '1000005926',
    '1000005927',
    '1000005928',
    '1000005929',
    '1000005930',
    '1000005931',
    '1000005932',
    '1000005933',
    '1000005934',
    '1000005937',
    '1000005938',
    '1000005940',
    '1000005941',
    '1000005942',
    '1000005943',
    '1000005944',
    '1000005945',
    '1000005946',
    '1000005947',
    '1000005948',
    '1000005949',
    '1000005950',
    '1000005951',
    '1000005952',
    '1000005953',
    '1000005954',
    '1000005955',
    '1000005956',
    '1000005957',
    '1000005958',
    '1000005959',
    '1000005960',
    '1000005961',
    '1000005962',
    '1000005963',
    '1000005964',
    '1000005965',
    '1000005966',
    '1000005967',
    '1000005968',
    '1000005969',
    '1000005970',
    '1000005971',
    '1000005972',
    '1000005973',
    '1000005974',
    '1000005975',
    '1000005976',
    '1000005977',
    '1000005978',
    '1000005979',
    '1000005980',
    '1000005981',
    '1000005982',
    '1000005983',
    '1000005984',
    '1000005985',
    '1000005986',
    '1000005987',
    '1000005988',
    '1000005989',
    '1000005990',
    '1000005991',
    '1000005992',
    '1000005993',
    '1000005994',
    '1000005995',
    '1000005996',
    '1000005997',
    '1000005998',
    '1000005999',
    '1000006000',
    '1000006001',
    '1000006002',
    '1000006003',
    '1000006004',
    '1000006005',
    '1000006006',
    '1000006007',
    '1000006008',
    '1000006009',
    '1000006010',
    '1000006011',
    '1000006012',
    '1000006013',
    '1000006014',
    '1000006015',
    '1000006016',
    '1000006017',
    '1000006018',
    '1000006019',
    '1000006020',
    '1000006021',
    '1000006022',
    '1000006023',
    '1000006024',
    '1000006025',
    '1000006026',
    '1000006027',
    '1000006028',
    '1000006029',
    '1000006030',
    '1000006031',
    '1000006032',
    '1000006033',
    '1000006035',
    '1000006036',
    '1000006037',
    '1000006038',
    '1000006039',
    '1000006040',
    '1000006041',
    '1000006042',
    '1000006043',
    '1000006044',
    '1000006045',
    '1000006046',
    '1000006047',
    '1000006048',
    '1000006049',
    '1000006050',
    '1000006051',
    '1000006052',
    '1000006053',
    '1000006054',
    '1000006055',
    '1000006056',
    '1000006057',
    '1000006059',
    '1000006060',
    '1000006061',
    '1000006062',
    '1000006063',
    '1000006064',
    '1000006065',
    '1000006066',
    '1000006067',
    '1000006068',
    '1000006069',
    '1000006070',
    '1000006071',
    '1000006072',
    '1000006073',
    '1000006074',
    '1000006075',
    '1000006076',
    '1000006077',
    '1000006078',
    '1000006079',
    '1000006080',
    '1000006081',
    '1000006082',
    '1000006083',
    '1000006084',
    '1000006085',
    '1000006086'
]
