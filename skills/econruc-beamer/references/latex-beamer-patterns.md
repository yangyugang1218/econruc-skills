# LaTeX Beamer Patterns

## Compilation

Use `latexmk -xelatex deck.tex` for Unicode, Chinese, and modern fonts.

Use `latexmk -pdf deck.tex` only when the deck is pure ASCII and already uses pdfLaTeX-compatible packages.

## Minimal frame patterns

Claim frame:

```tex
\begin{frame}{Claim-first title}
  \begin{wideitemize}
    \item Main economic claim
    \item Evidence or mechanism
    \item Boundary or implication
  \end{wideitemize}
\end{frame}
```

Figure plus takeaways:

```tex
\begin{frame}{Result title}
  \begin{columns}[T,onlytextwidth]
    \begin{column}{0.56\textwidth}
      \includegraphics[width=\linewidth]{figures/main_result.pdf}
    \end{column}
    \begin{column}{0.40\textwidth}
      \begin{wideitemize}
        \item Takeaway 1
        \item Takeaway 2
      \end{wideitemize}
    \end{column}
  \end{columns}
\end{frame}
```

Equation plus interpretation:

```tex
\begin{frame}{What identifies the key parameter?}
  \[
    y_{it} = \alpha_i + \delta_t + \beta D_{it} + X_{it}'\gamma + \varepsilon_{it}
  \]
  \vspace{0.5em}
  \begin{wideitemize}
    \item \blue{Identification:} compare changes in treated and control units
    \item \blue{Threat:} differential trends in unobserved shocks
  \end{wideitemize}
\end{frame}
```

Roadmap:

```tex
\begin{frame}{Outline}
  \begin{wideitemize}
    \item Motivation and research question
    \item Setting and data
    \item Identification and results
    \item Mechanisms and robustness
    \item Conclusion
  \end{wideitemize}
\end{frame}
```

## Appendix

Use:

```tex
\appendix
\backupbegin
...
\backupend
```

If using appendix page-number control from the template, backup slides should not inflate the main talk slide count.

## Tables

Prefer small tables:

- 3-5 rows
- 2-4 columns
- one coefficient family
- no tiny significance-star clutter unless essential

For full regression tables, put them in backup.
