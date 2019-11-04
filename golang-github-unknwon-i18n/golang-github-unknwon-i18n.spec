%global goipath         github.com/Unknwon/i18n
%global commit          b64d336589669d317928070e70ba0ae558f16633
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
