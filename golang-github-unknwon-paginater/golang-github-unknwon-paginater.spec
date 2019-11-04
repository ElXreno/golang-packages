%global goipath         github.com/Unknwon/paginater
%global commit          7748a72e01415173a27d79866b984328e7b0c12b
%global scm             git

%gometa

%global common_description %{expand:
Package i18n is for app Internationalization and Localization
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                0
Release:                1%{?dist}
Summary:                Package i18n is for app Internationalization and Localization

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
