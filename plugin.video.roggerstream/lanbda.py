exec("import re;import base64");print((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("MzIgPSAoJzE6Ly8wLjQvNi80YScpCjdkID0gKCcxOi8vMC40LzYvNTYnKQo3YyA9ICgnMTovLzAuNC82LzlhJykKN2IgPSAoJzE6Ly8wLjQvNi81MicpCjdhID0gKCcxOi8vMC40LzYvNTQnKQo3OSA9ICgnMTovLzAuNC82LzYwJykKNzggPSAoJzE6Ly8wLjQvNi80NycpCjc3ID0gKCcxOi8vMC40LzYvNWQnKQozMSA9ICgnMTovLzAuNC82LzUzJykKMmM9ICgnMTovLzAuNC82Lzk5JykKMjc9ICgnMTovLzAuNC82LzQ4JykKMjk9ICgnMTovLzAuNC82LzRmJykKMjg9ICgnMTovLzAuNC82LzVhJykKMjQ9ICgnMTovLzAuNC82LzVmJykKMjM9ICgnMTovLzAuNC82LzEzJykKMjY9ICgnMTovLzAuNC82LzViJykKMjU9ICgnMTovLzAuNC82LzVlJykKMmI9ICgnMTovLzAuNC82LzUxJykKMmE9ICgnMTovLzAuNC82LzRlJykKMjE9ICgnMTovLzAuNC82LzVjJykKMjI9ICgnMTovLzAuNC82LzRjJykKCjUwID0gMTIuOSgnMTA9PScpCjNkID0gMTIuOSgnOTg9JykKM2MgPSAxMi45KCc5ZCcpCjNlID0gMTIuOSgnZD0nKQo0NiA9IDEyLjkoJ2Y9JykKNDAgPSAxMi45KCc1PT0nKQozZiA9ICcxOi8vMC40LzYvJwo4ZCAzMCgpOgoJMygnW2JdMTEgNjkgOTYgMThbL2JdJywzMiw1NywnMTovLzkwLjcuMTQvNDQvNjYuOCcsMiwnJywnJywnJywnJykKCTMoJ1tiXTcyWy9iXScsMjIsNTcsJzE6Ly8zMy4yZC40LzMzLzFjLzdlLzhmLzdmLTZmLTgwLjgnLDIsJycsJycsJycsJycpCgkzKCdbYl05MyA4MSA0YlsvYl0nLDIxLDU3LCcxOi8vMWIuNy4xNC8zNy8xZC44JywyLCcnLCcnLCcnLCcnKQoJMygnW2JdODRbL2JdJywnLScsNTksJzE6Ly8xYi43LjE0LzNiLzg1LjgnLDIsJycsJycsJycsJycpCgkzKCdbYl03MCBlIDRkIFsxNiA1NV0gNzYgWy8xNl1bL2JdJywnLScsNjMsJzE6Ly8xYi43LjE0LzNhLzFhLjgnLDIsJycsJycsJycsJycpCQoJMygnW2JdOTcgODMgMThbL2JdJywnLScsNTgsJzE6Ly8zNi5jLjQvNjUuOCcsMiwnJywnJywnJywnJykKCTMoJ1tiXTM5IDgyIDg4IDgxIDRiWy9iXScsMjksNTcsJzE6Ly84Yi43LjE0LzQxLzE3LjgnLDIsJycsJycsJycsJycpCgkzKCdbYl0yMCAxOFsvYl0nLDJjLDU3LCcxOi8vMWIuNy4xNC8xOS8xNS44JywyLCcnLCcnLCcnLCcnKQoJMygnW2JdMTEgNjdbL2JdJywyOCw1NywnMTovLzM2LmMuNC82ZC44JywyLCcnLCcnLCcnLCcnKQoJMygnW2JdMTEgOTQgNjFbL2JdJywyNCw1NywnMTovLzM2LmMuNC82OC44JywyLCcnLCcnLCcnLCcnKQoJMygnW2JdMjAgNzVbL2JdJywyNyw1NywnMTovLzFiLjcuMTQvMTkvMTUuOCcsMiwnJywnJywnJywnJykKCTMoJ1tiXTExIFsxNiA1NV0gOTIgWy8xNl1bL2JdJywzMSw1NywnMTovLzM2LmMuNC82Yi44JywyLCcnLCcnLCcnLCcnKQoJMygnW2JdOWLDmjc0IGUgMmZbL2JdJywyMyw1NywnMTovLzM2LmMuNC82NC44JywyLCcnLCcnLCcnLCcnKQoJMygnW2JdNDkgMWZbL2JdJywyNiw1NywnMTovLzM2LmMuNC85NS44JywyLCcnLCcnLCcnLCcnKQoJMygnW2JdOWPDgTg2Wy9iXScsMjUsNTcsJzE6Ly8zNi5jLjQvNmMuOCcsMiwnJywnJywnJywnJykKCTMoJ1tiXTExIDQyWy9iXScsMmIsNTcsJzE6Ly8zNi5jLjQvNmEuOCcsMiwnJywnJywnJywnJykKCTMoJ1tiXTExIDgyIDg5w4dhWy9iXScsMmEsNTcsJzE6Ly8zNi5jLjQvNmUuOCcsMiwnJywnJywnJywnJykKCTMoIltiXTkxWy9iXSIsJy0nLDYyLCcxOi8vOGEuNy4xNC80NS83My44JywyLCcnLCcnLCcnLCcnKQoJMygiW2JdMzRbL2JdIiwnLScsNzEsJzE6Ly84Yy43LjE0LzQzLzM4LjgnLDIsJycsJycsJycsJycpCgk4Ny4xZSgnMzUuMmUoOGUpJykK")))(lambda a,b:b[int("0x"+a.group(1),16)],"pastebin|http|FANART|addDir|com|aHR0cDovL3d3dy5jYXJvbGluZW9saXZlaXJhLmNvbS5ici9zd2YvcGxheWVyLnN3Zg|raw|postimg|png|b64decode|A|B|imgur|aHR0cDovL3Bhc3RlYmluLmNvbS9yYXcvNmJ2Njh5N20|E|aHR0cDovL3d3dy5hb3Zpdm9icmFzaWwuY29tL3R2YW1pZ29zMi8|aHR0cDovL3R2LW1zbi5jb20vbWVzdHJlLnBocA|CANAIS|base64|X6rVNkmz|org|webcam_02_1|COLOR|android_marshmallow|BRASIL|scamereft|S_ries_e_desenhos|s20|robsonbillponte|futebol_ao_vivo|executebuiltin|INTERNACIONAIS|WEBCAMS|base20|base21|base15|base14|base17|base16|base11|base13|base12|base19|base18|base10|iconarchive|SetViewMode|VIDEOCLIPES|categorias|base9|base1|icons|FAVORITOS|Container|i|9nskrfnix|favorites|PROGRAMAS|ha5jgbkd5|hj3468x5l|url_base3|url_base2|url_base4|url_base7|url_base6|cxcndd31v|ITALIANOS|t22vlu68h|fg7t8j31n|xg55o044z|url_base5|QsCzHNGR|A0ykkpEb|ESPORTES|CbyvjZdT|VIVO|k7uzjLhW|DESENHOS|37FdgrtX|dN3zC3QX|url_base|ncqnVrD8|WNa0tcqT|ap4ydNNU|uHtcSkCC|blue|Lsw9Arc5|57|58|59|2kFUgBvU|JQA7GSTF|FjJ62Jqh|pfSLUDqy|ZqESM8yG|guVfkexz|BKXfruBC|PORTUGAL|62|63|mMaRel5|flYnDUu|century|LATINOS|zrN35DO|ABERTOS|2E2QDf1|A2ZUwkE|EQFgXqj|ODnHvr9|5oK0sUi|Movies|SERIES|71|FILMES|busca|SICAS|MUNDO|24hrs|base8|base7|base6|base5|base4|base3|base2|sinem|File|icon|AO|DA|PAGA|BRTV|brtv|DIOS|xbmc|BAND|FRAN|s29|s21|s24|def|500|256|s17|SEARCH|HD|FUTEBOL|DE|Wu97a7U|DO|TV|aHR0cDovL3R2LW1zbi5jb20vY2FuYWlzLmh0bWw|r81rtasw|sWHNJtKe|M|R|aHR0cDovL3d3dy50di1tc24uY29tL3BsYXllci9wbGF5ZXIuc3dm".split("|")))