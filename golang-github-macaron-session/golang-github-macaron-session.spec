%global goipath         github.com/go-macaron/session
%global commit          0a0a789bf1934e55fde19629869caa015a40c525
%global scm             git

%gometa

%global common_description %{expand:
Middleware session provides session management for Macaron
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                0
Release:                1%{?dist}
Summary:                Middleware session provides session management for Macaron

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
