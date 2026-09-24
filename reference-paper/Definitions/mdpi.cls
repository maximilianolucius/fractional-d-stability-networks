%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%	MDPI class for LaTeX files	 10 December 2025
%% %%	For any information please send an e-mail to:
%% %%		latex@mdpi.com
%% %%
%% %%	Initial class provided by:
%% %%		Stefano Mariani 
%% %%     Modified by:
%% %%		Dietrich Rordorf 
%% %%		Peter Harremoes 
%% %%		Zeno Schumacher 
%% %%		Maddalena Giulini 
%% %%		Andres Gartmann 
%% %%		Dr. Janine Daum 
%% %%		Xiu Li
%% %%     Versions:
%% %%		v1.0 before Dr. Janine Daum
%% %%		v2.0 when Dr. Janine Daum started (March 2013)
%% %%		v3.0 layout change September 2015
%%%%		v4.0 layout change December 2020
%%%%             v5.0 layout change December 2024
%%%%             v6.0 layout change December 2025
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%

%% IDENTIFICATION
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{Definitions/mdpi}[10/12/2025 MDPI paper class]

 %% PRELIMINARY DECLARATIONS
\LoadClass[10pt,a4paper]{article}
\RequirePackage[T1]{fontenc}
\RequirePackage[utf8]{inputenc}
\RequirePackage{calc}
\RequirePackage{indentfirst}
\RequirePackage{fancyhdr}
\RequirePackage{graphicx,epstopdf}
\RequirePackage{lastpage}
\RequirePackage{ifthen}
\RequirePackage{float}
\RequirePackage{amsmath}
\RequirePackage{amssymb} % For math environment bold format
\RequirePackage[right,mathlines]{lineno}
\RequirePackage{setspace}
\RequirePackage{enumitem}
\RequirePackage{mathpazo}
\RequirePackage{booktabs} % For \toprule etc. in tables
\RequirePackage{titlesec}
\RequirePackage{etoolbox} % For \AtBeginDocument etc.
\RequirePackage{tabto} % To use tab for alignment on first page
\RequirePackage{xcolor, colortbl} % To provide color for soul (for english editing), for adding cell color of table
\RequirePackage{soul} % To highlight text
\newcommand{\highlighting}[1]{\colorbox{yellow}{#1}}
\RequirePackage{multirow}
\RequirePackage{microtype} % For command \textls[]{}
\RequirePackage{tikz} % For \foreach used for Orcid icon
\RequirePackage{refcount} % To enable extracting the value of the counter "LastPage" 
\RequirePackage{changepage} % To adjust the width of the column for the title part and figures/tables (adjustwidth environment)
\RequirePackage{attrib} % For XML2PDF use \tag{} for equation
\RequirePackage{upgreek} % For making greek letters not italic
\RequirePackage{array} % For table array
\RequirePackage{tabularx}
\RequirePackage{pbox} % For biography environment
\RequirePackage{ragged2e} % For command \justifying
\RequirePackage[subfigure]{tocloft} % For dots in TOC. If subfigure package is loaded, the subfigure option needs to be added here to avoid clash: \RequirePackage[subfigure]{tocloft}
\RequirePackage{marginnote} % For left column
\reversemarginpar % To have the left column on the left side
\RequirePackage{marginfix} % For command \clearmargin for manually moving the left column to the next page
\RequirePackage{enotez} % For endnotes
\RequirePackage{xstring} % For citation in left column
\RequirePackage[labelformat=simple]{subfig} % Support to add subfigures
\renewcommand\thesubfigure{\normalfont(\textbf{\alph{subfigure}})} % Change subfigure label format

%% OPTIONS
% For transition period to change back to continuous page numbers
\def\@continuouspages{}
\newcommand{\continuouspages}[1]{\gdef\@continuouspages{#1}}

%% To choose the journal
% All journals (website name, full name, short name, DOI abbreviation, and ISSN + choice of continuous page numbers) are defined in an extra file. 
\input{Definitions/journalnames}
\DeclareOption{journal}{\ClassWarning{mdpi}{You used an invalid journal name or you have not specified the journal. The first option of the documentclass command specifies the journal. The word 'journal' should be replaced by one of the journal names specified in template.tex (in the comment 'Choose between the following MDPI journal').}} 

%% To choose the type of manuscript
\DeclareOption{abstract}{\gdef\@arttype{Abstract}}
\DeclareOption{addendum}{\gdef\@arttype{Addendum}}
\DeclareOption{article}{\gdef\@arttype{Article}}
\DeclareOption{benchmark}{\gdef\@arttype{Benchmark}}
\DeclareOption{book}{\gdef\@arttype{Book}}
\DeclareOption{bookreview}{\gdef\@arttype{Book Review}}
\DeclareOption{briefcommunication}{\gdef\@arttype{Brief Communication}}
\DeclareOption{briefreport}{\gdef\@arttype{Brief Report}}
\DeclareOption{casereport}{\gdef\@arttype{Case Report}}
\DeclareOption{changes}{\gdef\@arttype{Changes}}
\DeclareOption{clinicopathologicalchallenge}{\gdef\@arttype{Clinicopathological Challenge}}
\DeclareOption{comment}{\gdef\@arttype{Comment}}
\DeclareOption{commentary}{\gdef\@arttype{Commentary}}
\DeclareOption{communication}{\gdef\@arttype{Communication}}
\DeclareOption{conceptpaper}{\gdef\@arttype{Concept Paper}}
\DeclareOption{conferenceproceedings}{\gdef\@arttype{Proceedings}}
\DeclareOption{correction}{\gdef\@arttype{Correction}}
\DeclareOption{conferencereport}{\gdef\@arttype{Conference Report}}
\DeclareOption{creative}{\gdef\@arttype{Creative}}
\DeclareOption{datadescriptor}{\gdef\@arttype{Data Descriptor}}
\DeclareOption{discussion}{\gdef\@arttype{Discussion}}
\DeclareOption{entry}{\gdef\@arttype{Entry}}
\DeclareOption{expressionofconcern}{\gdef\@arttype{Expression of Concern}}
\DeclareOption{extendedabstract}{\gdef\@arttype{Extended Abstract}}
\DeclareOption{editorial}{\gdef\@arttype{Editorial}}
\DeclareOption{essay}{\gdef\@arttype{Essay}}
\DeclareOption{erratum}{\gdef\@arttype{Erratum}}
\DeclareOption{fieldguide}{\gdef\@arttype{Field Guide}}
\DeclareOption{hypothesis}{\gdef\@arttype{Hypothesis}}
\DeclareOption{interestingimages}{\gdef\@arttype{Interesting Images}}
\DeclareOption{letter}{\gdef\@arttype{Letter}}
\DeclareOption{meetingreport}{\gdef\@arttype{Meeting Report}}
\DeclareOption{monograph}{\gdef\@arttype{Monograph}}
\DeclareOption{newbookreceived}{\gdef\@arttype{New Book Received}}
\DeclareOption{obituary}{\gdef\@arttype{Obituary}}
\DeclareOption{opinion}{\gdef\@arttype{Opinion}}
\DeclareOption{proceedingpaper}{\gdef\@arttype{Proceeding Paper}}
\DeclareOption{projectreport}{\gdef\@arttype{Project Report}}
\DeclareOption{reply}{\gdef\@arttype{Reply}}
\DeclareOption{retraction}{\gdef\@arttype{Retraction}}
\DeclareOption{review}{\gdef\@arttype{Review}}
\DeclareOption{perspective}{\gdef\@arttype{Perspective}}
\DeclareOption{protocol}{\gdef\@arttype{Protocol}}
\DeclareOption{shortnote}{\gdef\@arttype{Short Note}}
\DeclareOption{studyprotocol}{\gdef\@arttype{Study Protocol}}
\DeclareOption{supfile}{\gdef\@arttype{Supfile}}
\DeclareOption{systematicreview}{\gdef\@arttype{Systematic Review}}
\DeclareOption{technicalnote}{\gdef\@arttype{Technical Note}}
\DeclareOption{viewpoint}{\gdef\@arttype{Viewpoint}}
\DeclareOption{guidelines}{\gdef\@arttype{Guidelines}}
\DeclareOption{registeredreport}{\gdef\@arttype{Registered Report}}
\DeclareOption{tutorial}{\gdef\@arttype{Tutorial}}
% Urology article types
\DeclareOption{giantsinurology}{\gdef\@arttype{Giants in Urology}}
\DeclareOption{urologyaroundtheworld}{\gdef\@arttype{Urology around the World}}
\DeclareOption{patentsummary}{\gdef\@arttype{Patent Summary}}

%% To choose the status of the manuscript
\DeclareOption{submit}{\gdef\@status{submit}}
\DeclareOption{accept}{\gdef\@status{accept}}

%% To choose the whether there is one or more authors
\DeclareOption{oneauthor}{\gdef\@authornum{author}}
\DeclareOption{moreauthors}{\gdef\@authornum{authors}}

%% Add the chosen options to the class
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}

%% Defaults
\ExecuteOptions{notspecified,10pt,a4paper,article,submit,oneauthor}

%% Process options
\ProcessOptions\relax

%% MORE DECLARATIONS

%%% Book contributions based on the article type
\newcommand{\isBookContribution}{%
	\ifthenelse{\equal{\@arttype}{Book}%
	\OR \equal{\@arttype}{Monograph}%
	}%
}

\newcommand{\isMonograph}{%
       \ifthenelse{\equal{\@arttype}{Monograph}%
	}%
}

\newcommand{\isPreprints}{%
        \ifthenelse{\equal{\@journal}{preprints}%
         \OR \equal{\@journal}{preprintschicago}%
         \OR \equal{\@journal}{preprintsapa}%
	}%
}

%%%% Maths environments
\RequirePackage{amsthm}
\newtheoremstyle{mdpi}% name
{12pt}% space above
{12pt}% space below
{\itshape}% body font
{}% indent amount 1
{\bfseries}% theorem head font
{.}% punctuation after theorem head
{.5em}% space after theorem head
{}% theorem head spec (can be left empty, meaning `normal')

\renewcommand{\qed}{\unskip\nobreak\quad\qedsymbol} %% This places the symbol right after the text instead of placing it at the end on the line.

\renewenvironment{proof}[1][\proofname]{\par %% \proofname allows to have "Proof of my theorem"
  \pushQED{\qed}%
  \normalfont \topsep6\p@\@plus6\p@\relax
  \trivlist
  \item[\hskip\labelsep
        \bfseries %% "Proof" is bold
    #1\@addpunct{.}]\ignorespaces %% Period instead of colon
}{%
  \popQED\endtrivlist\@endpefalse
}

 \theoremstyle{mdpi}
 \newcounter{theorem}
 \setcounter{theorem}{0}
 \newtheorem{Theorem}[theorem]{Theorem}
 
 \newcounter{lemma}
 \setcounter{lemma}{0}
 \newtheorem{Lemma}[lemma]{Lemma}
 
 \newcounter{corollary}
 \setcounter{corollary}{0}
 \newtheorem{Corollary}[corollary]{Corollary}
 
 \newcounter{proposition}
 \setcounter{proposition}{0}
 \newtheorem{Proposition}[proposition]{Proposition}
 
 \newcounter{characterization}
 \setcounter{characterization}{0}
 \newtheorem{Characterization}[characterization]{Characterization}
 
 \newcounter{property}
 \setcounter{property}{0}
 \newtheorem{Property}[property]{Property}
 
 \newcounter{problem}
 \setcounter{problem}{0}
 \newtheorem{Problem}[problem]{Problem}
 
 \newcounter{example}
 \setcounter{example}{0}
 \newtheorem{Example}[example]{Example}
 
 \newcounter{examplesanddefinitions}
 \setcounter{examplesanddefinitions}{0}
 \newtheorem{ExamplesandDefinitions}[examplesanddefinitions]{Examples and Definitions}
 
 \newcounter{remark}
 \setcounter{remark}{0}
 \newtheorem{Remark}[remark]{Remark}
 
 \newcounter{definition}
 \setcounter{definition}{0}
 \newtheorem{Definition}[definition]{Definition}
 
 \newcounter{hypothesis}
 \setcounter{hypothesis}{0}
 \newtheorem{Hypothesis}[hypothesis]{Hypothesis}

 \newcounter{notation}
 \setcounter{notation}{0}
 \newtheorem{Notation}[notation]{Notation}
 
 \newcounter{assumption}
 \setcounter{assumption}{0}
 \newtheorem{Assumption}[assumption]{Assumption}
 
 \newcounter{algorithm}
 \setcounter{algorithm}{0}
 \newtheorem{Algorithm}[algorithm]{Algorithm}
 
 % Define left/right mark in math environment
\let\originalleft\left
\let\originalright\right
\renewcommand{\left}{\mathopen{}\mathclose\bgroup\originalleft}
\renewcommand{\right}{\aftergroup\egroup\originalright} 

%%%% Chicago style journals
\newcommand{\isChicagoStyle}{
	\ifthenelse{\equal{\@journal}{arts}
		\OR \equal{\@journal}{genealogy}
		\OR \equal{\@journal}{histories}
		\OR \equal{\@journal}{humanities}
		\OR \equal{\@journal}{jintelligence}
		\OR \equal{\@journal}{laws}
		\OR \equal{\@journal}{literature}
		\OR \equal{\@journal}{religions}
		\OR \equal{\@journal}{risks}
		\OR \equal{\@journal}{socsci}
             \OR \equal{\@journal}{preprintschicago} %% Just use for preprints, not a real Chicago journal
             \OR \equal{\@journal}{chicagojournal} %% Just use for chicago submission, not a real Chicago journal
		}
}

%%%% APA style journals
\newcommand{\isAPAStyle}{
	\ifthenelse{\equal{\@journal}{admsci}       % Transfer to APA type
		\OR \equal{\@journal}{aieduc}       
		\OR \equal{\@journal}{behavsci}       % Transfer to APA type
		\OR \equal{\@journal}{businesses}    % Transfer to APA type
		\OR \equal{\@journal}{econometrics}% Transfer to APA type
		\OR \equal{\@journal}{economies}    % Transfer to APA type
		\OR \equal{\@journal}{education}     % Transfer to APA type
		\OR \equal{\@journal}{ejihpe}           % Transfer to APA type
		\OR \equal{\@journal}{famsci}           % Transfer to APA type
		\OR \equal{\@journal}{games}          % Transfer to APA type
		\OR \equal{\@journal}{humans}         % Transfer to APA type
		\OR \equal{\@journal}{ijcs}               % Transfer to APA type
		\OR \equal{\@journal}{ijfs}               % Transfer to APA type
		\OR \equal{\@journal}{journalmedia} % Transfer to APA type
		\OR \equal{\@journal}{jrfm}              % Transfer to APA type
		\OR \equal{\@journal}{jsam}             % New APA Journal
		\OR \equal{\@journal}{languages}      % Transfer to APA type
		\OR \equal{\@journal}{peacestud}      % New APA Journal
		\OR \equal{\@journal}{psycholint}      % Transfer to APA type
		\OR \equal{\@journal}{publications}   % Transfer to APA type
		\OR \equal{\@journal}{tourismhosp}   % Transfer to APA type
		\OR \equal{\@journal}{youth}             % Transfer to APA type
             \OR \equal{\@journal}{preprintsapa} %% Just use for preprints, not a real APA journal
             \OR \equal{\@journal}{apajournal} %% Just use for APA submission, not a real APA journal
		}
}

%%%% Chicago style journals
\newcommand{\isAPAandChicago}{
	\ifthenelse{\equal{\@journal}{arts}
		\OR \equal{\@journal}{genealogy}
		\OR \equal{\@journal}{histories}
		\OR \equal{\@journal}{humanities}
		\OR \equal{\@journal}{jintelligence}
		\OR \equal{\@journal}{laws}
		\OR \equal{\@journal}{literature}
		\OR \equal{\@journal}{religions}
		\OR \equal{\@journal}{risks}
		\OR \equal{\@journal}{socsci}
             \OR \equal{\@journal}{preprintschicago} 
	      \OR \equal{\@journal}{admsci}       
		\OR \equal{\@journal}{aieduc}      
		\OR \equal{\@journal}{behavsci}       
		\OR \equal{\@journal}{businesses}   
		\OR \equal{\@journal}{econometrics}
		\OR \equal{\@journal}{economies}    
		\OR \equal{\@journal}{education}     
		\OR \equal{\@journal}{ejihpe}    
		\OR \equal{\@journal}{famsci}       
		\OR \equal{\@journal}{games}          
		\OR \equal{\@journal}{humans}  
		\OR \equal{\@journal}{ijcs}                      
		\OR \equal{\@journal}{ijfs}              
		\OR \equal{\@journal}{journalmedia}
		\OR \equal{\@journal}{jrfm}             
		\OR \equal{\@journal}{jsam}
		\OR \equal{\@journal}{languages}
		\OR \equal{\@journal}{peacestud}
		\OR \equal{\@journal}{psycholint}      
		\OR \equal{\@journal}{publications}   
		\OR \equal{\@journal}{tourismhosp}   
		\OR \equal{\@journal}{youth}             
             \OR \equal{\@journal}{preprintsapa} 
             \OR \equal{\@journal}{chicagojournal} %% Just use for chicago submission, not a real Chicago journal
             \OR \equal{\@journal}{apajournal} %% Just use for APA submission, not a real APA journal
		}
}

%%%% References
\isAPAStyle{%
\RequirePackage[natbibapa]{Definitions/mdpi_apacite} % Only used for APA style journals
          }{%
          \RequirePackage[sort&compress,sectionbib]{natbib}
} % Option sectionbib is for optionally organizing references using sections (author request)

\renewcommand\NAT@set@cites{%
  \ifNAT@numbers
    \ifNAT@super \let\@cite\NAT@citesuper
       \def\NAT@mbox##1{\unskip\nobreak\textsuperscript{##1}}%
       \let\citeyearpar=\citeyear
       \let\NAT@space\relax
       \def\NAT@super@kern{\kern\p@}%
    \else
       \let\NAT@mbox=\mbox
       \let\@cite\NAT@citenum
       \let\NAT@space\relax
       \let\NAT@super@kern\relax
    \fi
    \let\@citex\NAT@citexnum
    \let\@biblabel\NAT@biblabelnum
    \let\@bibsetup\NAT@bibsetnum
    \renewcommand\NAT@idxtxt{\NAT@name\NAT@spacechar\NAT@open\NAT@num\NAT@close}%
    \def\natexlab##1{}%
    \def\NAT@penalty{\penalty\@m}%
  \else
    \let\@cite\NAT@cite
    \let\@citex\NAT@citex
    \let\@biblabel\NAT@biblabel
    \let\@bibsetup\NAT@bibsetup
    \let\NAT@space\NAT@spacechar
    \let\NAT@penalty\@empty
    \renewcommand\NAT@idxtxt{\NAT@name\NAT@spacechar\NAT@open\NAT@date\NAT@close}%
    \def\natexlab##1{##1}%
  \fi}

\isAPAStyle{%
      \bibliographystyle{Definitions/mdpi_apacite}
          }{%
              \isChicagoStyle{%
	        \bibliographystyle{Definitions/mdpi_chicago}
	        \bibpunct{(}{)}{;}{x}{}{,}%
	        }{%
	            \bibliographystyle{Definitions/mdpi}
	            \bibpunct{[}{]}{,}{n}{}{,}%
       }%
}

%%%%% Hyperlinks
%% Define color for citations
\definecolor{bluecite}{HTML}{0875b7}

%% crefname definitions
\newcommand{\crefnameDefinitions}{
	\crefname{figure}{Figure}{Figures}
	\crefname{table}{Table}{Tables}
	\crefname{section}{Section}{Sections}
	\crefname{appendix}{Appendix}{Appendices}
	\crefname{scheme}{Scheme}{Schemes}
	\crefname{chart}{Chart}{Charts}
	\crefname{paragraph}{Section}{Sections}
	\crefname{graph}{Graph}{Graphs}
}

% After TeXLive 2021, \AddToHook{begindocument} is needed to make sure that hyperref is loaded last. \ifdef{\AddToHook{begindocument}}{ is needed for backwards-compatibility because \AddToHook{begindocument} did not yet exist in 2020.
% After TeXLive 2022, \AddToHook{begindocument/before}{} is needed and  \DeclareHookRule{begindocument}{hyperref}{before}{mdpi} needs to be added because of the new version of hyperref.
\newcommand{\hyperrefpackage}{
      \isBookContribution{%
	\RequirePackage[unicode=true,
	bookmarksopen={true},
	pdffitwindow=true, 
	colorlinks=true, 
	linkcolor=black, 
	citecolor=black, 
	urlcolor=black, 
	hyperfootnotes=false, 
	pdfstartview={FitH},
	pdfpagemode=UseNone,
	pdfpagelabels]{hyperref}
	}{
	\ifthenelse{\equal{\@journal}{laws}}{
	\RequirePackage[unicode=true,
	bookmarksopen={true},
	pdffitwindow=true, 
	colorlinks=true, 
	linkcolor=bluecite, 
	citecolor=bluecite, 
	urlcolor=bluecite, 
	hyperfootnotes=false, 
	pdfstartview={FitH},
	pdfpagemode= UseNone]{hyperref}
	}{
	\RequirePackage[unicode=true,
	bookmarksopen={true},
	pdffitwindow=true, 
	colorlinks=true, 
	linkcolor=bluecite, 
	citecolor=bluecite, 
	urlcolor=bluecite, 
	hyperfootnotes=true, 
	pdfstartview={FitH},
	pdfversion=1.7,
	pdfpagemode= UseNone]{hyperref}
	} 
}
\RequirePackage[capitalise,noabbrev]{cleveref}
}
\ifdef{\AddToHook}{
\DeclareHookRule{begindocument}{hyperref}{before}{mdpi}
	\AddToHook{begindocument/before}{ 
		\hyperrefpackage
             \crefnameDefinitions
		}
	}{
	     \hyperrefpackage
           \crefnameDefinitions
}

\ifdefined\XeTeXversion
    \typeout{Check out XeLaTex!}
    \else
    \pdfminorversion=7  % Set PDF version
\fi

%% To have the possibility to change the urlcolor
\newcommand{\changeurlcolor}[1]{\hypersetup{urlcolor=#1}} 

%% Cleveref definitions
\newcommand{\cleverefDefinitions}{
	\crefrangelabelformat{figure}{##3##1##4--##5##2##6} % double # for nesting inside \newcommand
	\crefrangelabelformat{table}{##3##1##4--##5##2##6}
	\crefrangelabelformat{section}{##3##1##4--##5##2##6}	
	\crefrangelabelformat{appendix}{##3##1##4--##5##2##6}
	\crefrangelabelformat{scheme}{##3##1##4--##5##2##6}
	\crefrangelabelformat{chart}{##3##1##4--##5##2##6}
	\crefrangelabelformat{graph}{##3##1##4--##5##2##6}
}

\newcommand{\crefrangeconjunction}{--}
\newcommand{\fig}[1]{Figure~\ref{#1}}
\newcommand{\tabref}[1]{Table~\ref{#1}}
\newcommand{\sect}[1]{Section~\ref{#1}}
\newcommand{\app}[1]{Appendix~\ref{#1}}
\newcommand{\sche}[1]{Scheme~\ref{#1}}
\newcommand{\cchart}[1]{Chart~\ref{#1}}
\newcommand{\equ}[1]{\ref{#1}}
\newcommand{\boxref}[1]{Box~\ref{#1}}
\newcommand{\cgraph}[1]{Graph~\ref{#1}}

%%%% Metadata
\newcommand{\org@maketitle}{}% LATEX-Check
\let\org@maketitle\maketitle
\def\maketitle{%
	\hypersetup{
		pdftitle={\@Title},
		pdfsubject={\@abstract},
		pdfkeywords={\@keyword},
		pdfauthor={\@AuthorNames}
	}%
	\org@maketitle
}

%%%%% Endnotes
\setenotez{backref=true}
\DeclareInstance{enotez-list}{custom}{paragraph}{
	format=\fontsize{9}{11}\selectfont\leftskip0.76cm,
      number=\textsuperscript{\makebox[6mm][l]{#1}},
	notes-sep=0pt
}

%%%% Footnotes, for journal Laws
\RequirePackage{scrextend}
\setlength{\skip\footins}{0.6cm} % Increase space between text and footnote
\setlength{\footnotesep}{8pt} % Increase space between line and footnote
\deffootnote{1.5em}{0em}{\textsuperscript{\thefootnotemark}\quad} % Remove indent

%%%% Widows & orphans
\clubpenalty=10000
\widowpenalty=10000
\displaywidowpenalty=10000
\tolerance=1000 % slopiness / badness of the line breaking

%%%% To avoid "Output-loop.." compile bug
\maxdeadcycles=10000

% line and word spacing
\linespread{1.165}

% Indents & Commands for hanging indent
\setlength{\parindent}{0.75cm}
\newcommand{\dist}{1.7em}
\newcommand{\hang}{\hangafter=1\hangindent=\dist\noindent}

%%%% Front matter
% Command for checking for a question mark or exclamation mark in title
\def\instring#1#2{TT\fi\begingroup\edef\x{\endgroup\noexpand\in@{#1}{#2}}\x\ifin@}

\newcommand{\firstargument}{}
\newcommand{\Title}[1]{\gdef\@Title{#1}}%
\def\@Author{}
\newcommand{\Author}[1]{\gdef\@Author{#1}}%
\def\@AuthorNames{}
\newcommand{\AuthorNames}[1]{\gdef\@AuthorNames{#1}}%
\newcommand{\firstpage}[1]{\gdef\@firstpage{#1}}
\newcommand{\doinum}[1]{\gdef\@doinum{#1}}
\newcommand{\hreflink}[1]{\gdef\@hreflink{#1}}

% DOI number
% Create command to add a leading zero if 1 digit
\newcommand\twodigits[1]{%
	\ifnum#1<10 %
		0\number#1
   	\else
		\number#1
	\fi
}

% Create command to add a leading zero if less then 5 digits
\newcommand\fivedigits[1]{%
	\ifnum#1<10 %
		000\number#1
	\else
		\ifnum#1<100 %
			00\number#1
		\else
			\ifnum#1<1000 %
				0\number#1
			\else
				\ifnum#1<10000 %
					\number#1
				\else
					\ifnum#1<100000 %
						\number#1
					\else
						error
					\fi
				\fi
			\fi
		\fi
	\fi
}

\ifthenelse{\equal{\@journal}{molbank}
	\OR \equal{\@journal}{chemproc}
	\OR \equal{\@journal}{engproc}
	\OR \equal{\@journal}{eesp}
	\OR \equal{\@journal}{materproc}
	\OR \equal{\@journal}{blsf}
	\OR \equal{\@journal}{msf}
	\OR \equal{\@journal}{psf}
	\OR \equal{\@journal}{csmf}
	}{
	\doinum{10.3390/\@articlenumber}
	}{
	\doinum{10.3390/\@doiabbr\@pubvolume\twodigits\@issuenum\fivedigits\@articlenumber}
}

% For \@pubvolume, \@issuenum, and \@articlenumber: create command to cut leading zeros
\newcommand\cutdigits[1]{%
	\ifnum#1>0 %
		\number#1 
	\else
		\ifnum#1<10000 %
			\number#1
		\else             
			error
		\fi
	\fi
}

\newcommand{\pubvolume}[1]{\gdef\@pubvolume{\cutdigits{#1}}}
\newcommand{\pubyear}[1]{\gdef\@pubyear{#1}}
\newcommand{\copyrightyear}[1]{\gdef\@copyrightyear{#1}}
\newcommand{\address}[2][]{\renewcommand{\firstargument}{#1}\gdef\@address{#2}}
\newcommand{\corresfirstargument}{}
\def\@corres{}
\newcommand{\corres}[2][]{\renewcommand{\corresfirstargument}{#1}\gdef\@corres{#2}} 
\def\@conference{}
\newcommand{\conference}[1]{\gdef\@conference{#1}}%
\def\@abstract{}
\renewcommand{\abstract}[1]{\gdef\@abstract{#1}}
\def\@externaleditor{}
\newcommand{\externaleditor}[1]{\gdef\@externaleditor{#1}}
\def\@LSID{}
\newcommand{\LSID}[1]{\gdef\@LSID{#1}}
\def\@datereceived{}
\newcommand{\datereceived}[1]{\gdef\@datereceived{#1}} 
\def\@daterevised{}
\newcommand{\daterevised}[1]{\gdef\@daterevised{#1}} 
\def\@dateaccepted{}
\newcommand{\dateaccepted}[1]{\gdef\@dateaccepted{#1}} 
\newcommand{\datepublished}[1]{\gdef\@datepublished{#1}} 
\def\@datecorrected{}
\newcommand{\datecorrected}[1]{\gdef\@datecorrected{#1}}
\def\@dateretracted{}
\newcommand{\dateretracted}[1]{\gdef\@dateretracted{#1}}
\def\@pacs{}
\newcommand{\PACS}[1]{\gdef\@pacs{#1}} 
\def\@msc{}
\newcommand{\MSC}[1]{\gdef\@msc{#1}} 
\def\@jel{}
\newcommand{\JEL}[1]{\gdef\@jel{#1}}
\def\@keyword{}
\newcommand{\keyword}[1]{\gdef\@keyword{#1}}
\def\@dataset{}
\newcommand{\dataset}[1]{\gdef\@dataset{#1}}
\def\@datasetlicense{}
\newcommand{\datasetlicense}[1]{\gdef\@datasetlicense{#1}}
\def\@featuredapplication{}
\newcommand{\featuredapplication}[1]{\gdef\@featuredapplication{#1}}
\def\@keycontribution{}
\newcommand{\keycontribution}[1]{\gdef\@keycontribution{#1}}
\def\@issuenum{}
\newcommand{\issuenum}[1]{\gdef\@issuenum{\cutdigits{#1}}}
\def\@firstnote{}
\newcommand{\firstnote}[1]{\gdef\@firstnote{#1}}
\def\@secondnote{}
\newcommand{\secondnote}[1]{\gdef\@secondnote{#1}}%
\def\@thirdnote{}
\newcommand{\thirdnote}[1]{\gdef\@thirdnote{#1}}%
\def\@fourthnote{}
\newcommand{\fourthnote}[1]{\gdef\@fourthnote{#1}}%
\def\@fifthnote{}
\newcommand{\fifthnote}[1]{\gdef\@fifthnote{#1}}%
\def\@sixthnote{}
\newcommand{\sixthnote}[1]{\gdef\@sixthnote{#1}}%
\def\@seventhnote{}
\newcommand{\seventhnote}[1]{\gdef\@seventhnote{#1}}%
\def\@eighthnotes{}
\newcommand{\eighthnotes}[1]{\gdef\@eighthnotes{#1}}%
\def\@ninethnote{}
\newcommand{\ninethnote}[1]{\gdef\@ninethnote{#1}}%
\def\@tenthnote{}
\newcommand{\tenthnote}[1]{\gdef\@tenthnote{#1}}%
\def\@eleventhnote{}
\newcommand{\eleventhnote}[1]{\gdef\@eleventhnote{#1}}%
\def\@simplesumm{}
\newcommand{\simplesumm}[1]{\gdef\@simplesumm{#1}}
\newcommand{\articlenumber}[1]{
	\ifthenelse{\equal{\@journal}{molbank}}{
		\gdef\@articlenumber{#1}%
		}{
		\gdef\@articlenumber{\cutdigits{#1}}%
		}
	}

\def\@externalbibliography{}
\newcommand{\externalbibliography}[1]{\gdef\@externalbibliography{#1}}
\def\@reftitle{}
\newcommand{\reftitle}[1]{\gdef\@reftitle{#1}}
\def\@longauthorlist{}
\newcommand{\longauthorlist}[1]{\gdef\@longauthorlist{#1}}
\def\@encyclopediadef{}
\newcommand{\encyclopediadef}[1]{\gdef\@encyclopediadef{#1}}
\def\@addhighlights{}
\newcommand{\addhighlights}[1]{\gdef\@addhighlights{#1}}
\def\@CorrStatement{}
\newcommand{\CorrStatement}[1]{\gdef\@CorrStatement{#1}}
\newcommand{\textcorrstatement}{\textbf{Correction Statement:} This article has been republished with a minor change. The change does not affect the scientific content of the article and further details are available within the backmatter of the website version of this article.}
\def\@IsAssociation{}
\newcommand{\IsAssociation}[1]{\gdef\@IsAssociation{#1}}

%% ORCID
% Make Orcid icon
\newcommand{\orcidicon}{\includegraphics[width=0.32cm]{Definitions/logo-orcid.pdf}}

% Define link and button for each author
\foreach \x in {A, ..., Z}{%
\expandafter\xdef\csname orcid\x\endcsname{\noexpand\href{https://orcid.org/\csname orcidauthor\x\endcsname}{\noexpand\orcidicon}}
}

%%%% Journal name for the header
\newcommand{\journalname}{\@journalshort}

%%%% Header and footer on first page
%% The plain page style needs to be redefined because with \maketitle in the article class, LaTeX applies the the plain page style automatically to the first page.
\ifthenelse{\equal{\@journal}{preprints} %
		\OR \equal{\@journal}{preprintschicago}
		\OR \equal{\@journal}{preprintsapa}
		\OR \equal{\@arttype}{Book}
		\OR \equal{\@arttype}{Monograph}}{%
	\fancypagestyle{plain}{%
		\fancyhf{}
		\isPreprints{}{%
        		\fancyfoot[C]{\footnotesize\thepage}
        		}%
		}%
	}{%
	\ifthenelse{\equal{\@arttype}{Supfile}}{
		% page header and footer styles for supplementary files
		\fancypagestyle{plain}{
			\fancyhf{}
			\fancyhead[R]{
				\footnotesize %
				S\thepage{} of S\pageref*{LastPage}%
				\\\rule{\fulllength}{0.4pt}%
				}%
			\fancyhead[L]{
				\footnotesize %
				\ifthenelse{\equal{\@status}{submit}}{%
					Version {\@ \today} submitted to {\em \journalname}%
					}{%
					{\em \journalname} %
					{\bfseries \@pubyear}, %
					{\em \@pubvolume}, %
					\ifthenelse{\equal{\@continuouspages}{\@empty}}{%
						\@articlenumber%
						}{%
						S\@firstpage\ifnumcomp{\getpagerefnumber{LastPage}}{=}{\@firstpage}{}{--S\pageref*{LastPage}}%
						}%
					. {\url{https://doi.org/\@doinum}}%
					}%
					\\\vspace{-2pt}\rule{\fulllength}{0.4pt}%
				}%
			}%
		}{
		\fancypagestyle{plain}{
		\renewcommand{\footrulewidth}{0.4pt}
			\fancyhead{\null\vspace{8pt}}
			\fancyfoot[L]{
			\fontsize{8}{8}\selectfont
			\ifthenelse{\equal{\@status}{submit}}{%
				Version {\@ \today} submitted to {\em \journalname}%
				}{%
				{\em\journalname\ }{\bfseries\@pubyear}, {\em \@pubvolume}, %
				\ifthenelse{\equal{\@continuouspages}{\@empty}}{%
					\@articlenumber %
					}{%
					\@firstpage\ifnumcomp{\getpagerefnumber{LastPage}}{=}{\@firstpage}{}{--\pageref*{LastPage}} %
					}%
				}%
			}
			\fancyfoot[R]{
			\fontsize{8}{8}\selectfont
			{%
			}{\url{https://doi.org/\@doinum}}}%
		}
	}
}

%%%% Maketitle part 1: Logo, Arttype, Title, Author
\renewcommand{\@maketitle}{
	\isBookContribution{% for books we have no logos, article type and narrow column
            }{% for journals and preprints we have logos, article type and narrow column
		\ifthenelse{\equal{\@leftcolumnsplit}{\@empty}}{% Default option for the left column
			\marginnote[\contentleftcolumn]{}[\MyLen] % Bottom aligned
			}{%
		}
		\isPreprints{\vspace{0.92cm}}{%
		\begin{adjustwidth}{-\extralength}{}
		}
	}
	\begin{flushleft}
	\ifthenelse{\equal{\@arttype}{Supfile}}{%
		\fontsize{18}{18}\selectfont
		\raggedright
		\hyphenpenalty=10000
		\tolerance=1000
		\noindent\textbf{Supplementary Materials: \@Title}%
		\par
		\vspace{12pt}
		\fontsize{10}{10}\selectfont
		\noindent\boldmath\bfseries{\@Author}
		}{%
		\isBookContribution{}{%
			\vspace*{-1.75cm}
		}
		{%0
		\ifthenelse{\equal{\@journal}{preprints}
		\OR \equal{\@journal}{preprintschicago}
		\OR \equal{\@journal}{preprintsapa}
			\OR \equal{\@arttype}{Book}
			\OR \equal{\@arttype}{Monograph}}{}{
				\vspace{-2pt}%
				\ifthenelse{\equal{\@status}{submit}}{%	
				\vspace{5pt}%
					\hfill \href{https://www.mdpi.com}{%
					\includegraphics[height=1cm]{Definitions/logo-mdpi.eps}}%
					}{
					\href{https://www.mdpi.com/journal/\@journal}{
					\includegraphics[height=1.2cm]{Definitions/\@journal-logo.eps}}%
					\hfill
					\ifthenelse{\equal{\@IsAssociation}{\@empty} \OR \isundefined{\@IsAssociation}}{%
					\ifthenelse{\equal{\@journal}{ijom}}{%
						\href{https://www.mdpi.com}{\includegraphics[height=1cm]{Definitions/logo-mdpi-ijom.eps}}
						}{
					\ifthenelse{\equal{\@journal}{siuj}}{%
						\href{https://www.mdpi.com}{\includegraphics[height=1cm]{Definitions/logo-mdpi-siuj.eps}}
						}{
						\ifthenelse{\equal{\@journal}{scipharm}}{%
							\href{https://www.mdpi.com}{\includegraphics[height=1cm]{Definitions/logo-mdpi-scipharm.eps}}%
						}{%
							\href{https://www.mdpi.com}{\includegraphics[height=1cm]{Definitions/logo-mdpi.eps}}%
							}			
				                 }%				
				            }%				
				        }{	
				\href{https://www.mdpi.com}{\includegraphics[height=1cm]{Definitions/logo-mdpi-\@journal.eps}}%	
				      }%		
			      }%	
				\par
				\rule{\fulllength}{0.4pt}%
			}%
		\par
		}%0
		{%1
    		\vspace{14pt}
    		\fontsize{10}{10}\selectfont
		\isBookContribution{}{%
			\textit{\@arttype}%
			}%	
 	   	\par
    		}%1
    		{%2
  	  	\fontsize{18}{18}\selectfont
		\hyphenpenalty=10000
		\tolerance=1000
   	 	\isMonograph{}{%
   	 	       \boldmath\bfseries{\@Title}%
		       }%
   	 	\par
   	 	\vspace{12pt}
   	 	}%2
		\ifthenelse{\equal{\@longauthorlist}{\@empty}}{%
			}{%
			\end{flushleft}%
		\isPreprints{}{%
			\end{adjustwidth}%
			}
			\vspace{-2.5pt}
		}
   		{%3
		\hyphenpenalty=10000
		\tolerance=1000
   	 	\isMonograph{}{%
    		\boldmath\bfseries{\@Author}
             \ifthenelse{\equal{\@arttype}{Book}}{\vspace{-12pt}}{}
		       }%    		     
    		\par
		\vspace{12pt}
    		}%3
		}%
	\ifthenelse{\equal{\@longauthorlist}{\@empty}}{%
		\end{flushleft}%
		}{%
	}%
	\isBookContribution{}{%
		\ifthenelse{\equal{\@longauthorlist}{\@empty}}{%
		\isPreprints{}{%
			\end{adjustwidth}%
			}
			}{%
		}
	}
		\ifthenelse{\equal{\@leftcolumnsplit}{\@empty}}{% Left column split
			}{
			\marginnote[\contentleftcolumn]{}% Alignment with the affiliations
		}
	 \isMonograph{\vspace{-2cm}}{}	
	}

%%% Left column on first page (= "left column" = "leftcol")

% Definite font size for the narrow column
\newcommand{\leftcolFont}{%
	\linespread{1.71} 
	\fontsize{7}{7}\selectfont
	\justify
	\hyphenpenalty=10000
	\tolerance=1000
}

% Split content into six parts

% Part 1: Update logo
\newcommand{\leftcolumnUpdatelogo}{
	\leftcolFont
	\ifthenelse{\equal{\@status}{submit}}{
		}{%
		\href{https://crossmark.crossref.org/dialog?doi=\@doinum&domain=pdf&date_stamp=\the\year-\twodigits{\the\month}-\twodigits{\the\day}}{\includegraphics[height=.6cm]{Definitions/logo-updates.eps}}
	\vspace{-18pt}\\
		}%
}

%% Part 2: Academic editor(s)
\newcommand{\leftcolExternalEditor}{
	\ifthenelse{\equal{\@externaleditor}{\@empty}}{%
		}{%
		\leftcolFont
		\raggedright            
            \IfSubStr{\@externaleditor}{ and }{Academic Editors: \@externaleditor}{{\fontdimen2\font=1.4pt Academic Editor: \@externaleditor}}
            %\@externaleditor % For urgent situation, you can release this command and comment out line 953
	      \vspace{-4pt}	
	}
}

% Part 3: Dates
\newcommand{\leftcolDates}{
\isPreprints{%
	}{%
	\leftcolFont
	\ifthenelse{\equal{\@journal}{proceedings}
		\OR \equal{\@journal}{chemproc}
		\OR \equal{\@journal}{engproc}
		\OR \equal{\@journal}{eesp}
		\OR \equal{\@journal}{materproc}
		\OR \equal{\@journal}{blsf}
		\OR \equal{\@journal}{msf}
		\OR \equal{\@journal}{psf}
		\OR \equal{\@journal}{csmf}}{%
			Published: \@datepublished\\\vspace{-16pt}
			}{%
			Received: \@datereceived\\
			\ifthenelse{\equal{\@daterevised}{\@empty}}{%
				}{%
				Revised: \@daterevised\\%
				}
			Accepted: \@dateaccepted\\
			Published: \@datepublished
			\ifthenelse{\equal{\@datecorrected}{\@empty}}{%
				}{%
			\newline Corrected: \@datecorrected
			}
			\ifthenelse{\equal{\@dateretracted}{\@empty}}{%
				}{%
			\newline Retracted: \@dateretracted
			}\vspace{-4pt}
		}
	}
}

% Part 4: Correction statement
\newcommand{\leftcolumnCorrstatement}{%
\isPreprints{}{%
	\ifthenelse{\equal{\@CorrStatement}{yes}}{%
		\leftcolFont%
		\textcorrstatement%
             \vspace{-2pt}
		}{%
             \vspace{-2pt}
             }