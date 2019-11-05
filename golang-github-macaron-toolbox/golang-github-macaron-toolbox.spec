%global goipath         github.com/go-macaron/toolbox
%global commit          a77f45a7ce909c0ff14b28279fa1a2b674acb70f
%global scm             git

%gometa

%global common_description %{expand:
Middleware toolbox provides health chcek, pprof, profile and statistic services for Macaron.
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                0
Release:                1%{?dist}
Summary:                Middleware toolbox provides health chcek, pprof, profile and statistic services for Macaron.

License:                Apache-2.0
URL:                    %{gourl}
Source0:                %{gosource}


%description
%{common_description}

%gopkg


%prep
%goprep


%install
%gopkginstall


%files
%gopkgfiles



%changelog
* Mon Nov  4 2019 ElXreno <elxreno@gmail.com>
- Initial packaging
