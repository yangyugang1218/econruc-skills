* EconRUC graph defaults for Stata economics figures.
* Copy or include this file before graph commands when using Stata.

set scheme s2color
graph set window fontface "Arial"

global ECONRUC_INK        "34 34 34"
global ECONRUC_GRAY       "107 114 128"
global ECONRUC_LIGHTGRAY  "209 213 219"
global ECONRUC_BLUE       "47 107 154"
global ECONRUC_VERMILLION "182 74 58"
global ECONRUC_GREEN      "79 127 90"
global ECONRUC_GOLD       "182 138 45"

global ECONRUC_PAPER_OPTS ///
    graphregion(color(white)) ///
    plotregion(color(white) margin(zero)) ///
    bgcolor(white) ///
    legend(region(lcolor(none)) size(small)) ///
    ytitle(, size(small)) ///
    xtitle(, size(small)) ///
    ylabel(, labsize(small) angle(horizontal) nogrid) ///
    xlabel(, labsize(small)) ///
    yscale(lcolor(gs8)) ///
    xscale(lcolor(gs8))

global ECONRUC_REPORT_OPTS ///
    graphregion(color(white)) ///
    plotregion(color(white)) ///
    bgcolor(white) ///
    legend(region(lcolor(none)) size(medsmall)) ///
    ytitle(, size(medsmall)) ///
    xtitle(, size(medsmall)) ///
    ylabel(, labsize(medsmall) angle(horizontal) grid glcolor(gs14)) ///
    xlabel(, labsize(medsmall))

global ECONRUC_SLIDE_OPTS ///
    graphregion(color(white)) ///
    plotregion(color(white)) ///
    bgcolor(white) ///
    legend(region(lcolor(none)) size(medium)) ///
    title(, size(large) color("$ECONRUC_INK")) ///
    subtitle(, size(medsmall) color("$ECONRUC_GRAY")) ///
    ytitle(, size(medium)) ///
    xtitle(, size(medium)) ///
    ylabel(, labsize(medium) angle(horizontal) grid glcolor(gs14)) ///
    xlabel(, labsize(medium))

global ECONRUC_DIAGNOSTIC_OPTS ///
    graphregion(color(white)) ///
    plotregion(color(white)) ///
    bgcolor(white) ///
    legend(region(lcolor(none)) size(small)) ///
    ytitle(, size(small)) ///
    xtitle(, size(small)) ///
    ylabel(, labsize(small) angle(horizontal) grid glcolor(gs14)) ///
    xlabel(, labsize(small)) ///
    note(, size(vsmall) color("$ECONRUC_GRAY"))

* Example:
* twoway (rcap ci_low ci_high event_time, lcolor("$ECONRUC_BLUE")) ///
*        (scatter beta event_time, mcolor("$ECONRUC_BLUE")), ///
*        yline(0, lcolor(gs8)) xline(0, lpattern(dash) lcolor(gs10)) ///
*        $ECONRUC_PAPER_OPTS
