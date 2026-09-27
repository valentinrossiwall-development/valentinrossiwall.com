# Valentin Rossiwall · Website V2

Statische persönliche Website: Finance · Business Systems · Data & Technology.
HTML, CSS und ein kleines JavaScript für die mobile Navigation; kein Build-Schritt,
keine externen Fonts, Tracker oder automatisch geladenen Drittanbieter-Embeds.

## Lokal ansehen und prüfen

```sh
python3 -m http.server 8000 --bind 127.0.0.1
python3 scripts/check_site.py
```

Preview: http://127.0.0.1:8000

## Seitenstruktur

- `index.html`: Positionierung, Schwerpunkte und Einstiege
- `about.html`: persönliches Profil
- `erfahrung.html`: Erfahrungsfelder und historische Projekte
- `markets.html`: Research und persönliches Screening-Projekt
- `publikationen.html`: historische Publikationen und Medien, unter Markets eingeordnet
- `insights.html` und `insights/`: Blog und Artikel
- `kontakt.html`: direkter E-Mail-Kontakt; LinkedIn, bestätigtes GitHub-Profil und Website-Repository
- `unternehmertum.html`: Weiterleitung zur zusammengeführten Projektseite
- `impressum.html`, `datenschutz.html`: Anbieterangaben und Datenschutzerklärung für GitHub Pages

Navigation und Footer sind bewusst statisches HTML und auf allen Inhaltsseiten
identisch zu pflegen. Relative Links berücksichtigen die Unterordner der Artikel.
Kanonische Domain: https://valentinrossiwall.com (Home ohne index.html).

## Weitere Blog-Beiträge ergänzen

1. Den vorhandenen Artikel als HTML-Grundlage kopieren und einen neuen Dateinamen vergeben.
2. Inhalt, Titel, Description, Canonical, OpenGraph, Twitter und BlogPosting-JSON-LD
   vollständig anpassen. Nur bestätigte Veröffentlichungsdaten ergänzen.
3. Eine `article-card` nach folgendem Muster in `insights.html` ergänzen, den Beitrag
   im `blogPost`-Array des Blog-JSON-LD verknüpfen und in `sitemap.xml` aufnehmen.
4. Keine Platzhalterartikel verlinken; Vertraulichkeit und Quellen prüfen.
5. `python3 scripts/check_site.py` ausführen.

Die sichtbare Bezeichnung lautet überall **Blog**; `insights.html` und die bisherigen
Artikel-URLs bleiben unverändert. Kategorien: Finance, Business Systems,
Data & Analytics, Technology, Financial Markets und Entrepreneurship.
Die Themenliste ist eine Orientierung, kein Filter für noch nicht vorhandene Beiträge.

Kopiermuster für eine Karte ohne Medium (Platzhalter vor Verwendung vollständig ersetzen):

```html
<article class="article-card text-only" aria-labelledby="EINDEUTIGE-ID">
  <div class="article-copy">
    <div class="article-meta">
      <span class="eyebrow">KATEGORIE</span>
      <span>Veröffentlicht am <time datetime="YYYY-MM-DD">DATUM</time></span>
    </div>
    <h3 id="EINDEUTIGE-ID"><a href="insights/DATEINAME.html">TITEL</a></h3>
    <p>KURZBESCHREIBUNG</p>
    <a class="text-link" href="insights/DATEINAME.html">Artikel lesen</a>
  </div>
</article>
```

Das Datum auch auf der Artikelseite mit `<time>` und in JSON-LD pflegen:
`datePublished` nur bei bekanntem Veröffentlichungsdatum, `dateModified` bei einer
inhaltlichen Überarbeitung. Der bestehende Power-Query-Beitrag zeigt den tatsächlichen
Bearbeitungsstand vom 27. September 2026, kein erfundenes Erstveröffentlichungsdatum.
Sein `isPartOf` verweist auf den Blog. Diese Verknüpfung für weitere Beiträge übernehmen.

Optionales Bild/Video: `text-only` entfernen und vor `article-copy` ein
`<figure class="article-media">` mit Bild oder Video einfügen. Bilder mit passendem
Alternativtext, Breiten-/Höhenangaben und `loading="lazy"` versehen. Medienrechte prüfen.
Ohne Medium bleibt die Karte mit `text-only` über die volle Breite lesbar.

Videos können im Artikel mit `<video class="video" controls preload="none">`
und lokaler Quelle ergänzt werden. Untertitel mit `<track>` und ein Transkript
bereitstellen. Externe Videodienste erst nach Prüfung der Datenschutzhinweise
und mit einer bewussten Ladeaktion einbinden; die Klasse `video` ist vorbereitet.

## Vor Veröffentlichung offen

- Historische Rollen, Zeiträume, Projektnamen und Buchtitel final bestätigen.
  Die Website übernimmt ausschließlich Fakten aus dem bisherigen Repository.
- Power-Query-Beitrag redaktionell freigeben; das Beispiel ist ausdrücklich fiktiv.
- Erreichbarkeit von `contact@valentinrossiwall.com` vor dem Launch prüfen.
  GitHub-Profil `valentinrossiwall-development` wurde bestätigt.
- Optional: autorisierte Portrait-, Buch- und Social-Preview-Bilder sowie belegte Medienlinks ergänzen.
- Domain, HTTPS und bevorzugte Domainvariante beim Hosting konfigurieren; `/index.html`
  auf `/` und die bisherige Unternehmertums-URL auf `/erfahrung.html` serverseitig umleiten.
- Die entfernte Artikel-URL muss beim Hosting 404 oder 410 liefern, keine alte Cache-Kopie.
- Mobile/Desktop im Browser prüfen. Es sind keine Analytics oder Kontaktformulare eingebaut.

robots.txt und Sitemap verwenden die kanonische Domain. Die Rechtstexte sind
indexierbar und in der Sitemap enthalten. Hosting: GitHub Pages. Bei Änderungen
an Hosting, Kontaktfunktionen oder externen Medien die Datenschutzerklärung aktualisieren.

## Redaktionelle Leitplanken

Aktuelle Arbeit nur allgemein als Finance Operations, Business Systems, Data und
Process Improvement beschreiben. Frühere Selbstständigkeit und Beratung immer
historisch einordnen (2016–2024); keine Leistungsangebote oder Akquisitions-CTAs.
Kontakt dient fachlichem Austausch und beruflicher Vernetzung. Persönliche Datenprojekte
nicht als professionelle Software-Engineering-Leistung darstellen. Keine aktuellen
Arbeitgeber-, Kunden-, System- oder internen Projektangaben veröffentlichen.
