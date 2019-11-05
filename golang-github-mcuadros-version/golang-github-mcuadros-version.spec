%global goipath         github.com/mcuadros/go-version
%global commit          92cdf37c5b7579ebaf7a036da94b40995972088d
%global scm             git

%gometa

%global common_description %{expand:
Version normalizer and comparison library for Go.
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                0
Release:                1%{?dist}
Summary:                Version normalizer and comparison library for Go.

License:                MIT
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
