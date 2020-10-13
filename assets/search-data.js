'use strict';

(function () {
  const indexCfg = {{ with i18n "bookSearchConfig" }}
    {{ . }};
  {{ else }}
   {};
  {{ end }}

  indexCfg.doc = {
    id: 'id',
    field: ['title', 'content'],
    store: ['title', 'href', 'section'],
  };

  const index = FlexSearch.create('balance', indexCfg);
  window.bookSearchIndex = index;

  {{- $pages := where .Site.Pages "Kind" "in" (slice "page" "section") -}}
  {{- $pages = where $pages "Params.booksearchexclude" "!=" true -}}
  {{- $pages = where $pages "Content" "not in" (slice nil "") -}}

  {{ range $index, $page := $pages }}
  {{ $headers := findRE "<h[1-6].*?>(.|\n)+?<" .Content }}
  {{ $contents := findRE "</h[1-6]>(.|\n)*?(<h[1-6]|$)" .Content }}

  {{ range $i, $h := $headers }}
  index.add({
    'id': {{ add (mul $index 1000) $i }},
    'href': '{{ delimit (slice $page.RelPermalink ( $h | plainify | urlize )) "#" }}',
    'title': {{ $h | plainify | humanize | title | jsonify }},
    'section': {{ (path.Join (partial "docs/title" $page.Parent) (partial "docs/title" $page)) | jsonify }},
    'content': {{ (index $contents $i) | plainify | jsonify }}
  });
  {{ end }}
  {{- end -}}
})();
